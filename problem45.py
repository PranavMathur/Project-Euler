def triangle(n):
    return(n*(n+1)*(1/2))
def pentagonal(n):
    return(n*((3*n)-1)*(1/2))
def hexagonal(n):
    return(n*((2*n)-1))

def problem45():
    trilist = set()
    for i in reversed(range(285, 200000)):
        trilist.add(triangle(i))
    print("Computed all triangle values")
    pentlist = set()
    for o in reversed(range(165, 200000)):
        pentlist.add(pentagonal(o))
    print("Computed all pentagonal values")
    hexlist = set()
    for p in reversed(range(143, 200000)):
        hexlist.add(hexagonal(p))
    print("Computed all values. Now looking...")
    for q in hexlist:
        if q in pentlist:
            if q in trilist:
                print(q)
                
