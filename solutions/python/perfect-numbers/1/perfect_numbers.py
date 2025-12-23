import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    signature = sum(factors(number))
    if signature == number:
        return "perfect"
    if signature > number:
        return "abundant"
    return "deficient"
        
def factors(n):
    """return factors of n (n excluded)"""
    for i in range(1,n):
       if n%i == 0:
           yield i