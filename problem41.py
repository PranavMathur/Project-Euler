from itertools import *
from time import *
start = time()
nums = [str(i) for i in range(1, 10)]

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**.5)+2):
        if num%i == 0:
            return False
    return True

answer = 0

for j in ['1234', '1234567']:
    for i in permutations(j):
        a = int(''.join(i))
        if isPrime(a):
            if a > answer:
                answer = a

print(answer, time()-start)

            
