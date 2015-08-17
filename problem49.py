from itertools import *
from time import *
start = time()

primeFile = open('primeList.txt', 'r')

primes = [int(line) for line in primeFile if int(line) < 10000 and int(line) > 1000]

b = []

for i in range(0, 1060):
    for j in range(i+1, 1061):
        k = primes[j]+(primes[j]-primes[i])
        if k in primes:
            a = [int(q[0]+q[1]+q[2]+q[3]) for q in permutations(str(primes[i]), 4)]
            if primes[j] in a:
                if k in a:
                    b += [primes[i], primes[j], k]
                    print(primes[i], primes[j], k)

print(time()-start)
