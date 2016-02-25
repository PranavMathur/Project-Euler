from time import time
def fits(n):
    s = str(n)
    for i in range(-1, -18, -2):
        if int(s[i]) != int((i + 1) * .5) + 9:
            return False
    return True

def problem206():
    for i in range(101010107, 138902668, 10):
        if fits(i**2):
            return i

    for i in range(101010103, 138902664, 10):
        if fits(i**2):
            return i
    return 0

if __name__ == "__main__":
    start = time()
    print(problem206()*10, time() - start)
