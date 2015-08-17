from time import *
start = time()

def fracGen():
    a = [3, 2, 1]
    yield a
    while True:
        a = [a[0]+2*a[1], a[0]+a[1], a[2]+1]
        yield a

answer = 0

for i in fracGen():
    if i[2] > 1000:
        break
    if len(str(i[0])) > len(str(i[1])):
        answer += 1

print(answer, time()-start)

