primes = []
with open("bigprimes.list", "r") as f:
    for i in f.readlines():
        primes += [int(i)]