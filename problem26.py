from time import *
start = time()

def nines(num):
    n = '9'
    while True:
        if int(n)%num != 0:
            n += '0'
        else:
            return int(n)

ans = [0, 0]

for i in range(3, 1000, 2):
    if i%2 == 0 or i%5 == 0:
        continue
    if nines(i) > ans[1]:
        ans = [i, nines(i)]

print(ans, time()-start)
