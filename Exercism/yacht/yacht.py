def four_of_a_kind(dice):
    counts = {d: dice.count(d) for d in dice}
    if not max(counts.values()) >= 4:
        return 0
    return [d for d in counts if counts[d] == max(counts.values())][0] * 4


def ONES(dice): return sum(d for d in dice if d == 1)
def TWOS(dice): return sum(d for d in dice if d == 2)
def THREES(dice): return sum(d for d in dice if d == 3)
def FOURS(dice): return sum(d for d in dice if d == 4)
def FIVES(dice): return sum(d for d in dice if d == 5)
def SIXES(dice): return sum(d for d in dice if d == 6)
def FULL_HOUSE(dice): return sum(dice) if len(
    set(dice)) == 2 and dice.count(list(set(dice))[0]) in [2, 3] else 0


FOUR_OF_A_KIND = four_of_a_kind
def LITTLE_STRAIGHT(dice): return 30 if set(dice) == set(range(1, 6)) else 0
def BIG_STRAIGHT(dice): return 30 if set(dice) == set(range(2, 7)) else 0
def CHOICE(dice): return sum(dice)
def YACHT(dice): return 50 if len(set(dice)) == 1 else 0


"""
    Full House      Total of the dice       3 3 3 5 5 scores 19
    Four of a Kind  Total of the four dice  4 4 4 4 6 scores 16
"""


def score(dice, category):
    return category(dice)

#score([6, 6, 4, 6, 6], FOUR_OF_A_KIND)
