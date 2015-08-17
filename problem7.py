from math import *
from time import *
def isprime(x):
    
    

    a = sqrt(x)
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

def problem7():
    start = time()
    primes = [2, 3]
    for i in range (4, 2000000):
        if i % 6 == 1 or i % 6 == 5:
            if isprime(i) is True:
                primes += [i]
    print(primes[10000])
    end = time()
    print(end-start)
    return


            
