def is_valid(isbn):
    res = 0
    count = 10
    for x in isbn[:-1]:
        if x == '-':
            continue
        p = "0123456789".find(x)
        if p == -1:
            return False
        res += count*p
        count -= 1
    if count != 1:
        return False
    p = "0123456789X".find(isbn[-1])
    if p == -1:
        return False
    return (res+p)%11 == 0
        
