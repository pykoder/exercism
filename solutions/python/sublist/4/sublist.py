"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# I changed the constant to strings to make debugging and test failures easier to read
# No computing intensive operation involving these constants
EQUAL = "equal"
UNEQUAL = "unequal"
SUBLIST = "sublist"
SUPERLIST = "superlist"

def is_sublist(l1, l2) -> bool:
    for i in range(len(l2) - len(l1)):
        if l1[0] == l2[i] and l1[-1] == l2[i+len(l1)-1] and l1 == l2[i:i+len(l1)]:
            return True
    else:
        l2 = l2[-len(l1):]
    assert len(l1) == len(l2)
    return l1 == l2

def sublist(l1, l2):
    if not l1:
        return SUBLIST if l2 else EQUAL
    if not l2:
        return SUPERLIST
    if len(l1) == len(l2):
        return EQUAL if l1 == l2 else UNEQUAL
    if len(l1) < len(l2):
        return SUBLIST if is_sublist(l1, l2) else UNEQUAL
    return SUPERLIST if is_sublist(l2, l1) else UNEQUAL
