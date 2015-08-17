from itertools import *
from time import *
start = time()

def hasProperty(num):
    num = str(num)
    primes = [2, 3, 5, 7, 11, 13, 17]
    prime = 0
    for i in range(1, 8):
        a = int(num[i]+num[i+1]+num[i+2])
        if a % primes[prime] != 0:
            return False
        prime += 1
    return True

answer = 0

for i in permutations('0123456789'):
    i = ''.join(i)
    if int(i[3])%2 == 0:
        if hasProperty(i):
            answer += int(i)

print(answer, time()-start)
