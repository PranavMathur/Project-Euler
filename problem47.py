from time import *
beginning = time()

primes = [2]
start = 3

while time()-beginning <= 30:
    works = True
    for i in primes:
        if start%i == 0:
            works = False
            break
    if works:
        primes += [start]
    start += 2
    

def factors(num):
    orig = num
    primeFactors = set()
    for i in primes:
        if i > orig*.5:
            break
        if num%i == 0:
            primeFactors.add(i)
        while num%i == 0:
            num = num/i
    return len(primeFactors)
