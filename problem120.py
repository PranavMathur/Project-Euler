from time import time
start = time()

def f(a, n):
    return ((a-1)**n + (a+1)**n)%(a**2)
    
def rm(a):
    return max([f(a, n) for n in range(0, 2*a)])

print(sum([rm(i) for i in range(3, 1001)]), time()-start)