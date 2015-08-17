def digsum(x):
    y = str(x)
    k = 0
    for char in y:
        k += int(char)
    return(k)

def problem56():
    l = []
    for a in range(1, 100):
        for b in range(1, 100):
            j = a ** b
            f = digsum(j)
            l += [f]
    return(max(l))
    
