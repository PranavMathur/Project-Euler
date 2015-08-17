def isprime(x):
    a = x ** (1/2)
    b = a%1
    c = a - b
    d = int(c)
    for number in range(2, d + 3):
        if x%number == 0:
            return False
    return True

def problem10():
    add = 5
    for i in range(4, 2000000):
        if isprime(i) is True:
            add += i

    print(add)

