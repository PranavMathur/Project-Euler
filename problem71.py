from time import *

start = time()

closestDen = 0
closestNum = 0
closestDif = 1

for i in range(1, 1000001):
    if i%7 == 0:
        continue
    a = (3*i)/7
    a = int(a)
    dif = (3/7)-(a/i)
    if dif < closestDif:
        closestDif = dif
        closestDen = i
        closestNum = a

print(closestNum, time()-start)
