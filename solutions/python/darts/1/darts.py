import itertools

def score(x, y):
    r2 = x*x+y*y
    for d2, p in [(100,0), (25,1), (1,5)]:
        if r2 > d2:
            return p
    return 10
