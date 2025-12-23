def find_anagrams(word, candidates):
    nword = sorted(nn:=word.lower())
    return [x for x in candidates if sorted(n:=x.lower()) == nword and n != nn]
