# p40
import re
class make_xlat:
    def __init__(self, *args, **kwds):
        self.adict = dict(*args, **kwds)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.adict)))
    def one_xlat(self, match):
        return self.adict[match.group(0)]
    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

class make_xlat_by_whole_words(make_xlat):
    def make_rx(self):
        return re.compile(r'\b%s\b' % r'\b|\b'.join(map(re.escape, self.adict)))

class make_xlat_re(make_xlat):
    def make_rx(self):
        return re.compile('|'.join(self.adict))
    def dedictkey(self, text):
        for key in self.adict.keys():
            if re.search(key, text):
                return key
    def one_xlat(self, match):
        return self.adict[self.dedictkey(match.group(0))]

if __name__ == '__main__':
    text = "Larry Wall is the creator of Perl 123"
    adict = {
     "Larry Wall" : "Guido van Rossum",
     "creator" : "Benevolent Dictator for Life",
     "Perl" : "Python"
    }
    redict = {
     "Larry Wall" : "Guido van Rossum",
     "creator" : "Benevolent Dictator for Life",
     "(?:Perl|Ruby)" : "Python",
     "(\d+)" : "digits"
    }
    translate = make_xlat(adict)
    transwords = make_xlat_by_whole_words(adict)
    transre = make_xlat_re(redict)
    print translate(text)
    print transwords(text)
    print transre(text)
