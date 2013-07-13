# p35

def expand(format, d, marker='"', safe=False):
    if safe:
        def lookup(w): return d.get(w, w.join(marker*2))
    else:
        def lookup(w): return d[w]
    parts = format.split(marker)
    parts[1::2] = map(lookup, parts[1::2])
    return ''.join(parts)

if __name__ == '__main__':
    print expand('just "a" test', {'a':'one'})
    print expand('"a" "b" "c" "d"', {'a':'just', 'b':'one', 'c':'test'},safe=True)
    print expand('"a" "b" "c" "d"', {'a':'just', 'b':'one', 'c':'test'})

