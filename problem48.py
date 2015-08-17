import math
answer = 0
from time import *
start = time()
for i in range(1, 1001):
    answer += pow(i, i)
end = time()
print(str(answer)[-10:], end-start)
