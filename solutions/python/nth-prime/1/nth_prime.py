KNOWN_PRIMES = [2, 3, 5, 7, 11, 13]

def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    if type(number) != type(1) or number < 1:
        raise ValueError("Not an integer, we are expecting a positive integer")
    global KNOWN_PRIMES
    while len(KNOWN_PRIMES) < number:
        candidate = KNOWN_PRIMES[-1]+2
        while any(candidate % x == 0 for x in KNOWN_PRIMES):
            candidate += 2
        KNOWN_PRIMES.append(candidate)
    return KNOWN_PRIMES[number-1]