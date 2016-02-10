nums = {1000: 11, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 90: 6, 30: 6, 80: 6, 70: 7, 40: 5, 50: 5, 60: 5}

for i in range(100, 901, 100):
    a = i/100
    b = nums[a]
    c = b+7
    nums[i] = c

def separate(num):
    numlen = len(str(num))
    if numlen == 2:
        n1 = num%10
        n2 = num-n1
        return [n2, n1]
    if numlen == 3:
        n1 = num%10
        num = num - n1
        n2 = num%100
        n3 = num - n2
        return [n3, n2, n1]

def length(num):
    if len(str(num)) == 1:
        return nums[num]
    if len(str(num)) == 2:
        if 10 <= num <= 20 or num%10 == 0:
            return nums[num]
        lennum = 0
        a = num%10
        b = num - a
        c = nums[a] + nums[b]
        return c
    if len(str(num)) == 3:
        if num%100 == 0:
            return nums[num]
        a = num%100
        b = num - a
        return length(a) + nums[b] + 3
    else:
        return nums[num]
        
print(sum([length(i) for i in range(1, 1001)]))