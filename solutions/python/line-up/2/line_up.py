def suffix(number: int) -> str:
    """ Suffix is 
    - st if number ending in 1 unless 11
    - nd if number ending in 2 unless 12
    - nd if number ending in 3 unless 13
    for all others suffix is th
    """
    match number%10:
        case 1:
            return "st" if number%100 != 11 else "th"
        case 2:
            return "nd" if number%100 != 12 else "th"
        case 3:
            return "rd" if number%100 != 13 else "th"
        case _:
            return "th"

def line_up(name, number):
    return f"{name}, you are the {number}{suffix(number)} customer we serve today. Thank you!"