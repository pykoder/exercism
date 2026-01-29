KNOWN_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def primes():
    global KNOWN_PRIMES
    for n in KNOWN_PRIMES:
        yield n
    while True:
        candidate = KNOWN_PRIMES[-1]+2
        while any(candidate % x == 0 for x in KNOWN_PRIMES):
            candidate += 2
        KNOWN_PRIMES.append(candidate)
        yield candidate


def factors(value):
    if value == 1:
        return []
    result = []
    # Limit to 2000 first primes, we don't want to crash exercism infra
    for p, n in zip(primes(), range(2000)):
        while value % p == 0:
            result.append(p)
            value = value // p
        if value == 1:
            break
        if p*p > value:
             result.append(value)
             break
    return result
