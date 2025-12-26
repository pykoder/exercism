def commands(binary_str):
    """Given a string of 1s and 0s, return a list of commands corresponding to the secret handshake.

    The commands are determined by the following rules:
    - 1 (1st bit): "wink"
    - 10 (2nd bit): "double blink"
    - 100 (3rd bit): "close your eyes"
    - 1000 (4th bit): "jump"
    - 10000 (5th bit): Reverse the order of the commands

    Args:
        binary_str (str): A string representing a binary number.

    Returns:
        list: A list of commands corresponding to the secret handshake.
    """
    handshake_commands = [
        "wink",
        "double blink",
        "close your eyes",
        "jump"
    ]

    commands = []
    for i, bit in enumerate(binary_str[::-1]):
        if i == 5:
            commands.reverse()
            break
        if bit == '1':
            commands.append(handshake_commands[i-1])
    return commands
    
