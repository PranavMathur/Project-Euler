def isPalindrome(num):
    numstr = str(num)
    a = []
    q = []
    for character in numstr:
        a += [character]
    for character in numstr:
        q += [character]
    a.reverse()
    if a == q:
        return True
    return False

def change(num):
    answer = ''
    while num != 0:
        for i in reversed(range(0, 20)):
            a = 2**i
            if num >= a:
                answer += '1'
                num -= a
            else:
                answer += '0'
    return int(answer)

answer = 0

for i in range(1, 1000001):
    if isPalindrome(i):
        if isPalindrome(change(i)):
            answer += i
