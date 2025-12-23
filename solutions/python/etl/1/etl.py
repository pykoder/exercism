def transform(legacy_data):
    data = {}
    for value, letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = value
    return data