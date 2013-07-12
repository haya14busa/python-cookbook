# p7
thestring = 'hello world'

# method 1
thelist = list(thestring)

# method 2
for c in thestring:
    print c

# method 3
results = [c.upper() for c in thestring]
print results

# method 4
def plusA(string):
    print string
results = map(plusA, thestring)
