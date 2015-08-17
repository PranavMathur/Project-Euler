def pent(i):
    return i * (3 * i - 1) / 2

def problem44():
    e = []
    for f in range(1, 10001):
        e += [pent(f)]
    for q in e:
        for w in e:
            if q+w in e and abs(q-w) in e:
                print(q, w)
            
