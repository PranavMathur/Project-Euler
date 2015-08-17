def isprime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x == 3:
        return True
    a = x ** (1/2)
    b = a%1
    c = a - b
    d = int(c)
    for number in range(2, d + 3):
        if x%number == 0:
            return False
    return True

def istrue(i):
    if i % 2 == 0 or isprime(i) is True:
        return False
    for j in range(2, i - 1):
        if isprime(j) is True:
            v = i - j
            h = (v/2) ** (1/2)
            if h % 1 == 0:
                return True
    return False

def problem46():
    e = []
    for z in range(34, 10001):
        if z % 2 != 0 and isprime(z) is False:
            e += [z]
    for m in e:
        if istrue(m) is False:
            print(m)
        
            
        
    
                    
        
            
            
