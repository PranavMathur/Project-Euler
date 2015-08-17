import math
def problem20():
    x = math.factorial(100)
    y = str(x)
    answer = 0
    for char in y:
        answer += int(char)
    print(answer)

problem20()
