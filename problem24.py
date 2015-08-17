from itertools import *
from time import *

start = time()

a = [str(i) for i in range(0, 10)]

perms = []

for i in permutations(a):
    perms += [i]

perms.sort()

answer = ''

for char in perms[999999]:
    answer += char

print(answer)

end = time()

print(end-start)
