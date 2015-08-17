keylogF = open('keylog.txt', 'r')

keylog = []

for line in keylogF:
    keylog += [int(line)]

keylogF.close()
