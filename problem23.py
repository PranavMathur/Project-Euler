def factors(num):
    for i in range(1, int((num/2)+1)):
        if num % i == 0:
            yield i

def isAbundant(num):
    a = 0
    for i in factors(num):
        a += i
    if a > num:
        return True
    return False

abundant = []
answer = []

for i in range(1, 28124):
    answer += [i]
    if isAbundant(i):
        abundant += [i]


