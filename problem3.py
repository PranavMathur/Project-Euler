def isprime(x):
    a = x ** (1/2)
    #print(a)
    b = a%1
    #print(b)
    c = a - b
    #print(c)
    d = int(c)
    #print(d)
    for number in range(2, d + 3):
        #print(number)
        #print(x%number)
        if x%number == 0:
            return False
    return True

def factor(x):
    factors = []
    a = x ** (1/2)
    b = a%1
    c = a - b
    d = int(c)
    if isprime(x) is True:
        return x

    else:
        for number in range(2, d + 2):
            if x%number == 0 and isprime(number) is True:
                factors += [number]
        print(factors)
                
        




        
        
        
        
        
