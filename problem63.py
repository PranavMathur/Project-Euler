def istrue(x):
    y = str(x)
    h = len(y)
    if x ** (1/h) % 1 == 0:
        return True
    else:
        return False

def problem63():
    k = 0
    for i in range(1, 10000000000000000000000):
        if i % 500 == 0:
            print(i)
            
        if istrue(i) is True:
            k += 1
            print(k)
            
    
