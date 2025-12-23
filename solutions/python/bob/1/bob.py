import string

def response(hey_bob):
    last = hey_bob.strip()[-1:]
    letters = [l for l in hey_bob if l in string.ascii_letters]
    whitespace = [l for l in hey_bob if l not in string.whitespace]
    
    answers = [
    #This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
    (lambda: not whitespace,
     "Fine. Be that way!"),
    # This is what he says if you yell a question at him.
    (lambda: last == '?' 
         and letters
         and all([l in string.ascii_uppercase for l in letters]),
     "Calm down, I know what I'm doing!"),
    #This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    (lambda: last == '?',
     "Sure."),
     #This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    (lambda: letters and all([l in string.ascii_uppercase for l in letters]), "Whoa, chill out!"),
     #This is what he answers to anything else.
    (lambda: True, "Whatever.")]

    for check, reply in answers:
        if check():
            return reply

