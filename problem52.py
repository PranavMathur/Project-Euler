def issame(x, y):
    c = str(x)
    v = str(y)
    if len(c) != len(v):
        return False
    b = []
    n = []
    for char in c:
        b += [char]
    for char in v:
        n += [char]
    for i in b:
        if i not in n:
            return False
    for i in n:
        if i not in b:
            return False
    return True

def problem52():
    r = []
    for i in range(1, 1000000):
        q = set()
        for c in range(2, 7):
            q.add(c*i)
        w = 0
        for b in q:
            if issame(i, b) is False:
                w += 1
        if w == 0:
            print(i)
            
        
        
    
    
            
        
        
    
