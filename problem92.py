def square(num):
    answer = 0
    for character in str(num):
        answer += (int(character))**2
    return answer

def squareGen(num):
    while True:
        yield square(num)
        num = square(num)

def is89(num):
    for i in squareGen(num):
        if i == 89:
            return True
        if i == 1:
            return False

a = 0

for i in range(1, 10000000):
    if is89(i):
        a += 1
    if i%10000 == 0:
        print(i)
    
print(a)
        
