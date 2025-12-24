def label(colors):
    c2d = {
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
    power = c2d[colors[2]]
    total = (c2d[colors[0]] * 10 + c2d[colors[1]]) * 10**(power%3)
    if total >= 1000:
        total //= 1000
        power += 3
    unit = {
        0: "ohms",
        1: "kiloohms",
        2: "megaohms",
        3: "gigaohms"
    }[power//3]
    
    return f"{total} {unit}"
