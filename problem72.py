from time import time
from math import gcd
start = time()

count = 0
m = 1000

for d in range(m, 1, -1):
    for n in range(d - 1, 0, -1):
            i = 1
