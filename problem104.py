def fibGen(num):
    a = 1
    bNum = 1
    cNum = 1
    while a <= num:
        yield [bNum, a]
        a += 1
        yield [cNum, a]
        a += 1
        bNum += cNum
        cNum += bNum
        

def isPandigital(x):
    y = str(x)
    if '0' in y:
        return False
    for i in range(1, 10):
        b = str(i)
        if str(i) not in y:
            return False
    return True

def first(num):
    left = str(num)[:9]
    if isPandigital(int(left)):
        return True
    return False

def last(num):
    right = str(num)[-9:]
    if isPandigital(int(right)):
        return True
    return False



