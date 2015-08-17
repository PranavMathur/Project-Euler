from time import *
start = time()

def sequenceGen():
    k = 1
    while True:
        yield 1
        yield k * 2
        yield 1
        k += 1

sequence = []
current = 0
for i in sequenceGen():
    if current < 99:
        sequence += [i]
        current += 1
    else:
        break

sequence.reverse()

current = []

def manipulate(l, nextNum):
    l = [nextNum*l[1] + l[0], l[1]]
    l.reverse()
    return l

current = [1, sequence[0]]
sequence = sequence[1:]

while len(sequence) > 0:
    current = manipulate(current, sequence[0])
    sequence = sequence[1:]

current = [(2*current[1])+current[0], current[1]]

print(sum([int(i) for i in str(current[0])]), time()-start)

