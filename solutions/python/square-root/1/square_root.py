def square_root(number):
    for n in range(number,0,-1):
        if n*n <= number:
            return n
