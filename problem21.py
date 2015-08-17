def d(n):
    f = [1]
    for i in range(2, n):
        if n%i == 0:
            f += [i]
    return(sum(f))

def isamicable(x):
    y = d(x)
    if x == y:
        return False
    if d(y) == x:
        return True
    return False

def problem21():
    h = 0
    for i in range(1, 10001):
        if isamicable(i) is True:
            h += i
    print(h)




    

