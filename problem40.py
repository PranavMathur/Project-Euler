def problem40():
    i = '0.'
    w = []
    for f in range(1, 200000):
        i += str(f)
    for s in (2, 101, 1001, 10001, 100001, 1000001):
        d = i[s]
        print(d)
        e = int(d)
        w += [e]
    print(w)
    l = 1
    for z in w:
        l *= z
    print(l)
    


