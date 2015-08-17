def ocs(l, num):
    ans = 0
    for i in l:
        if i == num:
            ans += 1
    return ans

def isPandigital(num):
    if '0' in str(num):
        return False
    if len(str(num)) != 9:
        return False
    for char in str(num):
        if ocs(str(num), char) != 1:
            return False
    return True

def works1(num):
    for char in str(num):
        if ocs(str(num), char) != 1:
            return False
    return True

def works(f, s):
    if isPandigital(str(f)+str(s)+str(f*s)):
        return True
    return False

def maxProduct(num):
    a = 8 - len(str(num))
    b = int(a * '9')
    d = int(b/num)+1
    return d

answer = set()

for i in range(1, 100000000):
    if works1(i):
        for j in range(1, maxProduct(i)+1):
            if works(i, j):
                answer.add(i*j)
    
