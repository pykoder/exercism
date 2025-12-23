import string
def is_isogram(word):
    cleaned = [x for x in word.lower() if x in string.ascii_lowercase]
    return len(cleaned) == len(set(cleaned))
