from time import time
start = time()
nums = set()
primes = []
limit = 50000000
with open("primes.list", "r") as f:
    primes = [int(i) for i in f.readlines()]

for two in range(0, 78498):
    a = primes[two]**2
    if a > limit:
        break
    for three in range(0, 78498):
        b = a + (primes[three]**3)
        if b > limit:
            break
        for four in range(0, 78498):
            c = b + (primes[four]**4)
            if c > limit:
                break
            nums.add(c)

print(len(nums), time()-start)
