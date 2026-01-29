import re

def answer(question):
    if not question.startswith("What is "):
        raise ValueError("syntax error")
    question = question[len("What is "):]
    # Ensure question ends with question mark
    question = question[:-1]

    total = None
    is_value = False
    plus, minus, multiply_by, divide_by, multiply, divide = (False,)*6
    for token in question.split(' '):
        print(f"token {token}, total {total}")
        match token:
            case 'plus':
                if plus or minus or multiply_by or divide_by:
                    raise ValueError("syntax error")                    
                if total is None:
                    raise ValueError("syntax error")
                plus = True
                is_value = False
            case 'multiplied':
                if plus or minus or multiply_by or divide_by:
                    raise ValueError("syntax error")                    
                multiply = True
            case 'divided':
                divide = True
            case 'minus':
                if plus or minus or multiply_by or divide_by:
                    raise ValueError("syntax error")                    
                if total is None:
                    raise ValueError("syntax error")
                minus = True
                is_value = False
            case 'by' if divide:
                if plus or minus or multiply_by or divide_by:
                    raise ValueError("syntax error")                    
                if total is None:
                    raise ValueError("syntax error")
                divide_by = True
                is_value = False
            case 'by' if multiply:
                if plus or minus or multiply_by or divide_by:
                    raise ValueError("syntax error")                    
                if total is None:
                    raise ValueError("syntax error")
                multiply_by = True
                is_value = False
            case _ if re.match('^-?[\d]+$', token):
                if is_value:
                    raise ValueError("syntax error")                    
                value = int(token)
                is_value = True
                if total is None:
                    total = value
                elif minus:
                    minus = False
                    total -= value
                elif plus:
                    plus = False
                    total += value
                elif multiply_by:
                    multiply_by = False
                    total *= value
                elif divide_by:
                    divide_by = False
                    total /= value
            case _:
                raise ValueError("unknown operation")
    if plus or minus or multiply_by or divide_by or total is None:
        raise ValueError("syntax error")                    
    
    print(total)
    return total
