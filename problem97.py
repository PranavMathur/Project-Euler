from time import time
start = time()
current = 1
for exp in range(0, 7830457):
    current <<= 1
    current %= 10000000000

print((28433*current + 1)%10000000000, time() - start)
