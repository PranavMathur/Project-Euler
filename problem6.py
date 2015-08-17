def problem6(d):
    x = 0
    for i in range(1, d+1):
        x += (i**2)
    a = 0
    for h in range(1, d+1):
        a += h
    y = (a**2)
    print(x)
    print(y)
    print(y-x)
        
