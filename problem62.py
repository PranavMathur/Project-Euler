from itertools import *

found = False
start = 22

while not found:
    works = 0
    for i in permutations(str(start)):
        if (int(''.join(i))**(1/3))%1 == 0:
            works += 1
    if works == 3:
        print(start)
        found = True
    start += 1
    
