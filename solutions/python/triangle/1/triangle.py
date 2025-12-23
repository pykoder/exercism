def is_triangle(sides):
    a,b,c = sides
    return (a+b+c > 0) and (a + b > c) and (a + c > b) and (b + c > a)

def equilateral(sides):
    a,b,c = sides
    return a==b and b==c and is_triangle(sides)


def isosceles(sides):
    a,b,c = sides
    return (a==b or b==c or a==c) and is_triangle(sides)


def scalene(sides):
    return not (isosceles(sides) or equilateral(sides)) and is_triangle(sides)
