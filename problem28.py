def leftBot():
    c = 1
    a = 9
    b = 16
    ans = 0
    while c <= 500:
        ans += b
        b += 8
        c += 1
    return ans
