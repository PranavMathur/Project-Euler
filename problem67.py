import time
start = time.time()

file = open('problem67.txt', 'r')

triangle = []

def readLine(s):
    s = str(s)
    strlen = len(s)
    strlist = []
    a = 0
    while a <= strlen - 2:
        q = 10*int(s[a]) + int(s[a+1])
        strlist += [q]
        a += 3
    return strlist

for line in file:
    a = readLine(line)
    triangle.append(a)

current = 98

while current >= 0:
    currentList = triangle[current + 1]
    downList = triangle[current]
    for i in range(0, current+1):
        a = [currentList[i], currentList[i+1]]
        b = max(a)
        downList[i] += b
    triangle[current] = downList
    current -= 1

print(triangle[0], time.time() - start)
               


    
        
        
