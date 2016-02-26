limit = int(input())
primes = [True] * limit
for i in range(2, limit):
    if primes[i]:
        print(i)
        for j in range(2 * i, limit, i):
            primes[j] = False
