def isPrime(x):
    if x == 1:
        return False
    elif x == 2 or x ==3:
        return True
    a = x ** (1/2)
    b = a%1
    c = a - b
    d = int(c)
    for number in range(2, d + 3):
        if x%number == 0:
            
            return False
    return True

def leftGen(num):
    while len(str(num)) >= 1:
        num = str(num)
        yield int(num)
        num = num[1:]

def rightGen(num):
    while len(str(num)) >= 1:
        num = str(num)
        yield int(num)
        num = num[:-1]

a = 0
answer = 0
current = 11

def truncR(num):
    for i in rightGen(num):
        if not isPrime(i):
            return False
    return True

def truncL(num):
    for i in leftGen(num):
        if not isPrime(i):
            return False
    return True

while a <= 11:
    if truncL(current):
        if truncR(current):
            print(current)
            answer += current
            a += 1
    current += 1


