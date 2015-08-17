numFile = open('base_exp.txt', 'r')
numList = []
for line in numFile:
    numList.append([int(i.split('\n')[0]) for i in line.split(',')])


numFile.close()

currentBig = 
