def sequence(i):
    x = 1
    y = [i]
    while i != 1:
        if i % 2 == 0:
            i = i/2
        else:
            i = (3 * i) + 1
        x += 1
        y += [i]
    return(x)
    
    


        
       
    
def problem14():
    f = {}
    for c in range (2, 1000000):
        x = sequence(c)
        f[x] = c
    a = max(f)
    b = f[a]
    return(b)
    
    
        
        

        
    
    




    
        
    


        
    
