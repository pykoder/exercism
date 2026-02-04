def units(n: int):
    if not (0 <= n < 10):
        raise ValueError(f"dizain out of range {n}")
        
    return ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine"][n]

def dizains(n: int):
    if not (0 <= n < 10):
        raise ValueError(f"dizain out of range {n}")
    return ["zero", "teen", "twenty", "thirty", "forty", 
            "fifty", "sixty", "seventy", "eighty", "ninety"][n]

def tokenize_hundredth(n: int):
    if not (0 <= n < 1000):
        raise ValueError(f"number out of range {n}")

    hundredth = ""
    if n >= 100:
        hundredth = f"{units(n // 100)} hundred"
        n %= 100
    if n == 0:
        lower_2_digits = ""
    elif 1 <= n <= 9:
        lower_2_digits = units(n)
    elif 10 <= n <= 12:
         lower_2_digits = ["ten", "eleven", "twelve"][n-10]
    elif n < 20:
         lower_2_digits = ["thirteen", "fourteen", "fivteen", "sixteen",
                          "seventeen", "eighteen", "nineteen"
                         ][n-13]
    else:
        lower_digit = n%10
        if lower_digit > 0:
            lower_2_digits = f"{dizains(n//10)}-{units(lower_digit)}"
        else:
            lower_2_digits = f"{dizains(n//10)}"

    return [hundredth, lower_2_digits]

def say(number: int):
    if not (0 <= number < 1_000_000_000_000):
        raise ValueError("input out of range")
        
    if number == 0:
        return "zero"

    english_number = []
    if number >= 1_000_000_000:
        english_number.extend(tokenize_hundredth(number // 1_000_000_000))
        english_number.append("billion")
        number %= 1_000_000_000
    if number >= 1_000_000:
        english_number.extend(tokenize_hundredth(number // 1_000_000))
        english_number.append("million")
        number %= 1_000_000
    if number >= 1_000:
        english_number.extend(tokenize_hundredth(number // 1_000))
        english_number.append("thousand")
        number %= 1_000
    english_number.extend(tokenize_hundredth(number))
    
        
    return " ".join([x for x in english_number if x])
    
