# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == YACHT:
        return 50 if dice.count(dice[0]) == 5 else 0
    elif 1 <= category <= 6:
        return dice.count(category)*category
    elif category == FULL_HOUSE:
        sd = sorted(dice)
        return sum(sd) if (sd[0] != sd[-1]
            and sd.count(sd[0]) in [2, 3]
            and sd.count(sd[-1]) == 5 - sd.count(sd[0])) else 0
    elif category == FOUR_OF_A_KIND:
        sd = sorted(dice)
        if sd.count(sd[0]) >= 4:
            return sd[0]*4
        if sd.count(sd[-1]) == 4:
            return sd[-1]*4
        return 0
    elif category == LITTLE_STRAIGHT:
        sd = sorted(dice)
        if sd == [1,2,3,4,5]:
            return 30
        return 0
    elif category == BIG_STRAIGHT:
        sd = sorted(dice)
        if sd == [2,3,4,5,6]:
            return 30
        return 0
    else:
        return sum(dice)
