def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**.5)+2):
        if num%i == 0:
            return False
    return True

def family(num):
    
