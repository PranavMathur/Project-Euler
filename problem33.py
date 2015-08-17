def works(num, den):
    return (str(num)[1] == str(den)[0]) and den%10 != 0 and (int(num/10)/(den%10) == num/den)
    
for i in range(10, 100):
    for j in range(i+1, 100):
        if works(i, j):
            print(i, j)
