
from email.mime import text

def atbash(text):
    return ''.join(("zyxwvutsrqponmlkjihgfedcba")[ord(c) - ord('a')]
                    if c.isalpha() else c 
                    for c in text.lower() if c.isalnum())

def encode(plain_text):
    text = atbash(plain_text)
    return ' '.join([text[i:i+5] for i in range(0, len(text), 5)])


def decode(ciphered_text):
    return atbash(ciphered_text)
