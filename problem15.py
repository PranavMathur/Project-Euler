def factorial(num):
    answer = 1
    while num >= 1:
        answer = answer*num
        num -=  1
    return answer

def combination(n, k):
    a = factorial(n)
    b = factorial(k)
    c = n - k
    d = factorial(c)
    e = b * d
    f = a/e
    return f

print(combination(40, 20))
