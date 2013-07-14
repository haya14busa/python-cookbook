# p39
import re
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat

if __name__ == '__main__':
    text = "Larry Wall is the creator of Perl"
    adict = {
     "Larry Wall" : "Guido van Rossum",
     "creator" : "Benevolent Dictator for Life",
     "Perl" : "Python"
    }
    print multiple_replace(text, adict)
    translate = make_xlat(adict)
    print translate(text)

