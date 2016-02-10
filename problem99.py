from time import time
start = time()
from math import log
def logPair(a, b):
    return log(a) * b

pairs = []

with open("base_exp.txt", "r") as f:
    for line in f.readlines():
        s = line.strip().split(",")
        pairs += [[int(i) for i in s]]

maxNum = 0
maxIndex = 0
i = 0
while i < 1000:
    pair = pairs[i]
    if logPair(pair[0], pair[1]) > maxNum:
        maxNum = logPair(pair[0], pair[1])
        maxIndex = i
    i += 1
    
print(maxIndex + 1, time() - start)
