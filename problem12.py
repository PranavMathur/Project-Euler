def triangleGen():
    triangle = 1
    currentAdd = 2
    while True:
        yield triangle
        triangle += currentAdd
        currentAdd += 1

def factors(num):
    factors = [1, num]
    for i in range(2, round(num/2)+1):
        if num%i == 0:
            factors += [i]
    return factors


