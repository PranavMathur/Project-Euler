"""row1 = [75]
row2 = [95, 64]
row3 = [17, 47, 82]
row4 = [18, 35, 87, 10]
row5 = [20, 4, 82, 47, 65]
row6 = [19, 1, 23, 75, 3, 34]
row7 = [88, 2, 77, 73, 7, 63, 67]
row8 = [99, 65, 4, 28, 6, 16, 70, 92]
row9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
row10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
row11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
row12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
row13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
row14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
row15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15]

finalList = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
backList = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(0, 14):
    a = [row15[i], row15[i+1]]
    b = max(a)
    row14[i] += b

for i in range(0, 13):
    a = [row14[i], row14[i+1]]
    b = max(a)
    row13[i] += b

for i in range(0, 12):
    a = [row13[i], row13[i+1]]
    b = max(a)
    row12[i] += b

for i in range(0, 11):
    a = [row12[i], row12[i+1]]
    b = max(a)
    row11[i] += b

for i in range(0, 10):
    a = [row11[i], row11[i+1]]
    b = max(a)
    row10[i] += b

for i in range(0, 9):
    a = [row10[i], row10[i+1]]
    b = max(a)
    row9[i] += b

for i in range(0, 8):
    a = [row9[i], row9[i+1]]
    b = max(a)
    row8[i] += b

for i in range(0, 7):
    a = [row8[i], row8[i+1]]
    b = max(a)
    row7[i] += b

for i in range(0, 6):
    a = [row7[i], row7[i+1]]
    b = max(a)
    row6[i] += b

for i in range(0, 5):
    a = [row6[i], row6[i+1]]
    b = max(a)
    row5[i] += b

for i in range(0, 4):
    a = [row5[i], row5[i+1]]
    b = max(a)
    row4[i] += b

for i in range(0, 3):
    a = [row4[i], row4[i+1]]
    b = max(a)
    row3[i] += b

for i in range(0, 2):
    a = [row3[i], row3[i+1]]
    b = max(a)
    row2[i] += b

for i in range(0, 1):
    a = [row2[i], row2[i+1]]
    b = max(a)
    row1[i] += b"""

file = open('problem18.txt', 'r')

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

current = 13

while current >= 0:
    currentList = triangle[current + 1]
    downList = triangle[current]
    for i in range(0, current+1):
        a = [currentList[i], currentList[i+1]]
        b = max(a)
        downList[i] += b
    triangle[current] = downList
    current -= 1

    
        

