# p19
import string
def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans('', '')
        delete = allchars.translate(allchars, keep.translate(allchars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate

#### Example ###
digits_only = translator(keep=string.digits)
print digits_only('Chris Perkins : 224-7992')

no_digits = translator(delete=string.digits)
print no_digits('Chris Perkins : 224-7992')

digits_to_hash = translator(frm=string.digits, to='#')
print digits_to_hash('Chris Perkins : 224-7992')


