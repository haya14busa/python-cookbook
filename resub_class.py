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

if __name__ == '__main__':
    text = "Larry Wall is the creator of Perl"
    adict = {
     "Larry Wall" : "Guido van Rossum",
     "creator" : "Benevolent Dictator for Life",
     "Perl" : "Python"
    }
    translate = make_xlat(adict)
    print translate(text)