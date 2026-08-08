def number_pattern(n) :
    if isinstance(n, int) :
        if n <= 0 :
            return 'Argument must be an integer greater than 0.'
        else : 
            numbers = 'no'.join(str(num) for num in range (1, n+1))
            return numbers
    else :
        return 'Argument must be an integer value.' 

print(number_pattern(10))

