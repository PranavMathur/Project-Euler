from time import *
begin = time()

def findQuad(l):
    p = l[0]
    q = l[1]
    r = l[2]
    c = p
    a = (r-p-2*(q-p))/2
    b = q-a-c
    return [a, b, c]

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**.5)+2):
        if num%i == 0:
            return False
    return True

def evaluate(l, num):
    ans = 0
    current = 2
    for i in l:
        ans += (num**current)*i
        current -= 1
    return ans

def ratio(l):
    composites = ((len(l)-1)/3)
    primes = 0
    for i in l:
        if isPrime(i):
            primes += 1
        else:
            composites += 1
    return primes/(composites+primes)


rud = findQuad([3, 13, 31])
lud = findQuad([5, 17, 37])
lld = findQuad([7, 21, 43])

diagonals = [1]


found = False

size = 1
current = 0

##while not found:
##    for d in [rud, lud, lld]:
##        diagonals += [evaluate(d, current)]
##    size += 2
##    current += 1
##    if ratio(diagonals) <= .1:
##        print(size, time()-begin)
##        found = True


