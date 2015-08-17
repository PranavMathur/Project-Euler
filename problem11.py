from time import *
start = time()
file = open('problem11.txt', 'r')

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

squareRows = []
squareColumns = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
answer = 0

for line in file:
    a = readLine(line)
    squareRows.append(a)

for i in range(0, 20):
    for row in squareRows:
        squareColumns[i] += [row[i]]

for row in squareRows:
    for i in range(0, 17):
        product = row[i]*row[i+1]*row[i+2]*row[i+3]
        if answer < product:
            answer = product

for row in squareColumns:
    for i in range(0, 17):
        product = row[i]*row[i+1]*row[i+2]*row[i+3]
        if answer < product:
            answer = product

for row in range(0, 17):
    for col in range(0, 17):
        row1 = squareRows[row]
        row2 = squareRows[row+1]
        row3 = squareRows[row+2]
        row4 = squareRows[row+3]
        product = row1[col]*row2[col+1]*row3[col+2]*row4[col+3]
        if answer < product:
            answer = product

for row in range(3, 17):
    for col in range(3, 17):
        row1 = squareRows[row]
        row2 = squareRows[row-1]
        row3 = squareRows[row-2]
        row4 = squareRows[row-3]
        product = row1[col]*row2[col+1]*row3[col+2]*row4[col+3]
        if answer < product:
            answer = product
        
print(product)
end = time()
print(end-start)


        















