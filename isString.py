# p10
def isStringLike(anobj):
    try: anobj + ''
    except: return False
    else: return True

print isStringLike(1)
print isStringLike('1')
