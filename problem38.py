from time import *
start = time()

def isPandigital(num):
    if len(str(num)) != 9:
        return False
    if '0' in str(num):
        return False
    for i in range(1, 10):
        if str(i) not in str(num):
            return False
    return True

def works(num, end):
    products = ''
    for i in range(1, end+1):
        products += str(num*i)
    if isPandigital(int(products)):
        return True
    return False

answer = 0

for i in range(1, 50000):
    end = 2
    length = 0
    while length <= 9:
        products = ''
        for j in range(1, end+1):
            products += str(i*j)
        if isPandigital(products):
            if int(products) > answer:
                answer = int(products)
        length = len(products)
        end += 1

print(answer, time() - start)
