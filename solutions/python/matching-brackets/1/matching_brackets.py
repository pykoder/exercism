def is_paired(input_string):
    stack = []
    for x in input_string:
        if x in '[{(':
            stack.append(x)
            continue
        p = ']})'.find(x)
        if p >= 0:
            if not stack or stack[-1] != '[{('[p]:
                return False
            stack.pop()
    return len(stack) == 0