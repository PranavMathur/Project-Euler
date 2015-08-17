def add3and5():
    answer = 0
    for number in range(1, 1000):
        if number%3 == 0 or number%5 == 0:
            answer += number
    return(answer)

        
