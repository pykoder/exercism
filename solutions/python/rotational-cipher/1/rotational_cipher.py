from string import ascii_lowercase, ascii_uppercase
llet = ascii_lowercase
ulet = ascii_uppercase

def rotate(text, key):
    for let in (llet, ulet):
        trans = str.maketrans(let, let[key:]+let[:key])
        text = text.translate(trans)
    return text
        