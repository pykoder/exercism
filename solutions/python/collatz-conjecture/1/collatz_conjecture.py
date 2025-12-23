def steps(number):
    try:
        if number <= 0:
            raise  
        n = int(number)
    except:
        raise ValueError("Only positive integers are allowed")
    def fly_time(n):
        if n&1:
            if n == 1:
                return 0
            return 1 + fly_time(3*n+1)
        return 1 + fly_time(n//2)
    return fly_time(n)
