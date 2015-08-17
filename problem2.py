
def f(x):
    if x == 1:
        return(1)
    elif x == 2:
        return(2)
    elif x > 0:
        return(f(x-2) + f(x-1))
    else:
        print("I don't know")

def fib(x, y):
    for i in range(x, y+1):
        print(f(i))
        print(i)
                          

def addfibonacci():
    answer = 0
    for number in range(1, 33):
        term = f(number)
        if term%2 == 0:
            answer += term
    print(answer)


    
        
        
    
    
    
