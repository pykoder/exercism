
C2D = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

UNIT = {
    0: "ohms",
    1: "kiloohms",
    2: "megaohms",
    3: "gigaohms"
}

TOLERANCE = {
    "brown": "±1%",
    "red": "±2%",
    "green": "±0.5%",
    "blue": "±0.25%",
    "violet": "±0.1%",
    "grey": "±0.05%",
    "gold": "±5%",
    "silver": "±10%"
}


def label(colors):
    """ Compute value and unit of resistance from color bands. 
    works for 3, or 4 color bands
    and monocolor black band (0 ohms) 
    """
    power = C2D[colors[-1]]
    total = 0
    for color in colors[:-1]:
        total = total * 10 + C2D[color]
    total *= 10**(power%3)

    # if total > 1000, convert to next unit
    if total >= 1000:
        # If exact multiple of 1000, result is integer not float
        # as we want values like 1 kiloohms not 1.0 kiloohms
        if total % 1000 == 0:
            total //= 1000
        else:
            total /= 1000.0
        power += 3
    unit = UNIT[power//3]   
    return f"{total} {unit}"

def resistor_label(colors):
    """Compute value and unit of resistance from color bands,
    with tolerance if applicable.
    works for 1, 3, 4, or 5 color bands
    """
    if len(colors) > 3:
        base_label = label(colors[:-1])
        tolerance = TOLERANCE.get(colors[-1], "")
        return f"{base_label} {tolerance}"
    return label(colors)
