from time import *
start = time()

primes = []
primeF = open("primeList.txt", "r")
for i in primeF:
   primes += [int(i)]
   
primeSums = [2]

current = 1

l = len(primes)
while primeSums[len(primeSums) - 1] < 1000000:
   primeSums += [primeSums[len(primeSums)-1] + primes[current]]
   current += 1
   
print(primeSums[len(primeSums)-2], 997661 in primes)

# current = l-1
# 
# greatest = 0
# 
# while current > 1:
#    print(current)
#    current2 = l-1
#    while current2 > 0:
#       if primeSums[current] - primeSums[current2] in primes and primeSums[current]-primeSums[current2] > greatest:
#          print(primeSums[current], primeSums[current2], primeSums[current]-primeSums[current2])
#          greatest = primeSums[current]-primeSums[current2]
#       current2 -= 2