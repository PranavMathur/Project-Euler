from time import time

start = time()

def l(i):
    return len(str(i))

c = 0
for base in range(1, 10):
    for exp in range(1, base + 13):
        if l(base**exp) == exp:
            c += 1

print(time() - start)
print(c)
