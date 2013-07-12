# p10
def isStringLike(anobj):
    try: anobj + ''
    # try: anobj.lower() + anobj + ''
    except: return False
    else: return True

print isStringLike(1)
print isStringLike('1')
