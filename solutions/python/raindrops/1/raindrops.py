def convert(number):
    sound = ""
    for n, l in [(3, "i"), (5, "a"), (7, "o")]:
        if number % n == 0:
            sound += f"Pl{l}ng"
    if not sound:
        sound = f"{number}"
    return sound
        