def problem30():
    e = []
    for i in range(2, 1000000):
        f = str(i)
        c = 0
        for char in f:
            d = int(char)
            c += (d ** 5)
        if i == c:
            e += [i]
            print(i, c)
    print(sum(e))
problem30()
