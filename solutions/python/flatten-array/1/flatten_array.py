def flatten(iterable):
    result = []
    try:
        for x in [x for x in iterable]:
            result.extend(flatten(x))
    except TypeError:
        if iterable is not None:
            result.append(iterable)
    return result
