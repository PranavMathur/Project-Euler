def problem29():
    f = []
    for i in range(2, 101):
        for v in range(2, 101):
            c = i ** v
            if c not in f:
                f += [c]
    return(len(f))
