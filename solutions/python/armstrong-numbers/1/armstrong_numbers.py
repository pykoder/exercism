def is_armstrong_number(number):
    digits = []
    x = number
    while x >= 10:
        digits.append(x%10)
        x //= 10
    digits.append(x)
    return number == sum([x**len(digits) for x in digits])
