def problem16():
    x = 2 ** 1000
    y = str(x)
    answer = 0
    for char in y:
        answer += int(char)
    print(answer)

problem16()
