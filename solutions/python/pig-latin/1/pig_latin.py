def translate(text):
    pig = []
    for word in text.split():
        if word[:1] in 'aeiou' or word[:2] in ["xr", "yt"]:
            pass
        elif word[:3] in ['squ', 'thr', 'sch']:
            word = word[3:]+word[:3]
        elif word[:2] in ['ch', 'qu', 'th', 'rh']:
            word = word[2:]+word[:2]
        else:
            word = word[1:]+word[:1]
        pig.append(word+"ay")
    return " ".join(pig)
