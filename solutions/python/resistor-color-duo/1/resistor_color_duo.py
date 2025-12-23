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

def value(colors):
    return COLOR_CODES[colors[1].title()]+ 10 * COLOR_CODES[colors[0].title()]
