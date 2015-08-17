import time
start = time.time()
def fibGen():
    a = 1
    bNum = 1
    cNum = 1
    while True:
        yield [bNum, a]
        a += 1
        yield [cNum, a]
        a += 1
        bNum += cNum
        cNum += bNum

for i in fibGen():
    if len(str(i[0])) == 1000:
        print(i[1])
        break
end = time.time()
print(end-start)
