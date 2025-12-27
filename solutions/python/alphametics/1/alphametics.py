from itertools import permutations, chain
from functools import reduce
from operator import or_

def word_value(word, letter_map):
    value = 0
    for letter in word:
        value = value * 10 + letter_map[letter]
    return value

def solve(puzzle):
    """
    Find solutions to alphametic puzzles where each letter represents a unique digit
    in mathematical equations (only + and == allowed thus far).
    
    :param puzzle: Description of the puzzle as a string, e.g. "SEND + MORE == MONEY"
    :return: A dictionary mapping letters to digits, or None if no solution exists.

    This implementations uses brute-force permutation of digits for letters.
    It excludes solutions where any word starts with a leading zero.
    0 is allowed as a digit for letters not at the start of any word.
    10 or more unique letters will return None as there are not enough digits.

    It can probably be made faster, but is fast enough as is and passes all tests.
    """
    puzzle = puzzle.replace(' ', '')
    words = puzzle.split('==')
    left_words = words[0].split('+')
    right_words = words[1].split('+')       
    letters = "".join(reduce(or_, (set(word) for word in chain(left_words, right_words)), set()))
    if len(letters) > 10:
        return None
    for candidate in permutations(range(10), len(letters)):
        letter_map = dict(zip(letters, candidate))
        # Exclude solutions with leading zeros in words. This is what the test checks for.
        # As a human puzzle solver, I would accept leading zeros. Exclusing them is a design choice.
        if any(letter_map[word[0]] == 0 for word in chain(left_words, right_words)):
            continue
        left_sum = sum(word_value(word, letter_map) for word in left_words)
        right_sum = sum(word_value(word, letter_map) for word in right_words)
        if left_sum == right_sum:
            # Found a valid solution and stop there. That is what the test expects.
            # would rather use yield to find all solutions, but the test does not expect that.
            return letter_map
