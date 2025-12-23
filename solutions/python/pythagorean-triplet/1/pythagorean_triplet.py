def triplets_with_sum(number):
    result = []
    for a in range(1, number):
        for b in range(a,number):
            c  = number - a - b
            if c < b:
                break
            if a**2+b**2 == c**2:
                result.append([a,b,c])
    return result