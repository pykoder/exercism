def suffix(number: int) -> str:
    """ Suffix is 
    - st if number ending in 1 unless 11
    - nd if number ending in 2 unless 12
    - nd if number ending in 3 unless 13
    for all others suffix is th
    """
    final_digits_pair = number % 100
    if final_digits_pair in [11, 12, 13]:
        return "th"
    final_digit = number % 10       
    return ["th", "st", "nd", "rd", *("th",)*6][final_digit]


def line_up(name, number):
    return f"{name}, you are the {number}{suffix(number)} customer we serve today. Thank you!"