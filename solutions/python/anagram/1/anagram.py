def find_anagrams(word, candidates):
    nword = sorted(nn:=word.lower())
    return filter(lambda x: sorted(n:=x.lower()) == nword and n != nn, candidates)
