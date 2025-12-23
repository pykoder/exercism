def sum_of_multiples(limit, multiples):
    s = set()
    for l in set(multiples):
      if l > 0:
        m = l
        while m < limit:
            s.add(m)
            m += l
    return sum(s)
        
