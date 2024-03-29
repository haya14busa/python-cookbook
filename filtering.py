# p22

import string

allchars = string.maketrans('', '')
def makefilter(keep):
    delchars = allchars.translate(allchars, keep)

    # def thefilter(s):
    #     return s.translate(allchars, delchars)
    # return thefilter
    return lambda s: s.translate(allchars, delchars)


def canonicform(s):
    return makefilter(s)(allchars) #s->keep, allchars->filterd letters

if __name__ == '__main__':
    just_vowels = makefilter('aeiouy')
    print just_vowels('four score and seven years ago')
    print just_vowels('tiger, tiger burning bright')

    print canonicform('hayabusa')
    # test = makefilter('hayabusa')(allchars)
    # print test
    # print just_vowels(allchars)
