def f(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return(r)

def c(n, r):
    c = f(n)
    v = f(r)
    b = f((n-r))
    return(c/(v*b))

def problem53():
    p = 0
    for a in range(6, 101):
        for s in range(1, a):
            if c(a, s) > 1000000:
                p += 1
    print(p)
