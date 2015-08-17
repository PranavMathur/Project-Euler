def triangle(i):
    return((1/2) * i * (i+1))

def lettervalue(a):
    x = str(a)
    c = 1
    h = {}
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        h[char] = c
        c += 1
    e = h[a]
    return(e)

def wordvalue(a):
    s = str(a.replace("\"",""))
    d = 0
    for char in s:
        d += int(lettervalue(char))
    return(d)

def problem42():
    myFile = open('words.txt', 'r')
    t = []
    for words in myFile:
        for word in words.split(","):
           t += [int(wordvalue(str(word)))]
    q = []
    for v in range(1, 25):
        q += [triangle(v)]
    y = 0
    for hi in t:
        if hi in q:
            y += 1
    print(t)
    print(y)
    
           
    
    
