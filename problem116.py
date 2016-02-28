reds = [0, 0, 1]
greens = [0, 0, 0, 1]
blues = [0, 0, 0, 0, 1]
for i in range(3, 51):
    count = 0
    for j in range(0, i-1):
        count += (reds[j] + 1)
    reds += [count]
    
for i in range(4, 51):
    count = 0
    for j in range(0, i-2):
        count += (greens[j] + 1)
    greens += [count]
    
for i in range(5, 51):
    count = 0
    for j in range(0, i-3):
        count += (blues[j] + 1)
    blues += [count]
