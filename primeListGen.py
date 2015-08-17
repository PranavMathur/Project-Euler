primes = [2]

current = 3

primeListf = open('primeList.txt', 'w')
primeListf.write(str(2)+'\n')

while True:
    prime = True
    for i in primes:
        if current%i == 0:
            prime = False
            break
    if prime:
        primes += [current]
        primeListf.write(str(current)+'\n')
    current += 2
    
