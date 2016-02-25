wayArr = [0, 1, 1, 2] + [0]*100
d = 1
for i in range(4, 5):
    ways = 0
    for j in range(1, int(i/2)+1):
        ways += wayArr[j] + wayArr[i-j]
        print(j, i-j)
    wayArr[i] = ways
