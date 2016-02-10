squares = [i**2 for i in range(0, 100000)]

def findSol(d):
    for y in range(1, 2000):
        

m = 0

d = 2
ld = 0
while d < 1001:
    if d in squares:
        pass
    else:
        print(d)
        ma = min([i for i in findSol(d)])
        print(d)
        if ma != None and ma > m:
            m = ma
            ld = d
            print(m, d)
    d += 1
