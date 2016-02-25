limit = 5
reds = [0] * limit
lastStart = 0
for i in range(0, limit - 1):
    reds[i] = 1 + reds[i-1]
