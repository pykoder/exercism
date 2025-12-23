COLOR_CODES = {'Black': 0, 
            'Brown': 1, 
            'Red': 2, 
            'Orange': 3, 
            'Yellow': 4, 
            'Green': 5, 
            'Blue': 6, 
            'Violet': 7, 
            'Grey': 8, 
            'White': 9}
CODE_COLORS = dict((code,color) for color, code in COLOR_CODES.items())

def color_code(color):
    """
    input: a color name as string
    result: numerical value of that color following the mapping below
    Black: 0,  Brown: 1, Red: 2, Orange: 3, Yellow: 4, Green: 5, Blue: 6, Violet: 7, Grey: 8, White: 9
    """
    return COLOR_CODES[color.title()]

def colors():
    return [CODE_COLORS[code].lower() for code in range(0, 10)]
        
