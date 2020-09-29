from copy import deepcopy
from itertools import product
from pprint import pprint


HOUSE_ID = list(range(5))
COLORS = ['red', 'green', 'ivory', 'yellow', 'blue']
NATIONS = ['Englishman', 'Japanese', 'Norwegian', 'Spaniard', 'Ukrainian']
PETS = ['dog', 'fox', 'horse', 'snail', 'zebra']
DRINKS = ['coffee', 'milk', 'orange', 'tea', 'water']
SMOKES = ['Chesterfields', 'Kools', 'Lucky Strike', 'Old Gold', 'Parliaments']


def not_both(key1, val1, key2, val2):
    return (key1 == val1 and key2 != val2) or (key2 == val2 and key1 != val1)


def neighbour_pet(hostid, candidate):
    pets = []
    if hostid != 0:
        pets.append(candidate[hostid-1][3])
    if hostid != 4:
        pets.append(candidate[hostid+1][3])
    return set(pets)


def validate_simple(case):
    house_id, color, nation, pet, drink, smoke = case
    if not_both(nation, 'Englishman', color, 'red'):            # 2.
        return False
    if not_both(nation, 'Spaniard', pet, 'dog'):                # 3.
        return False
    if not_both(drink, 'coffee', color, 'green'):               # 4.
        return False
    if not_both(nation, 'Ukrainian', drink, 'tea'):             # 5.
        return False
    if not_both(smoke, 'Old Gold', pet, 'snail'):               # 7.
        return False
    if not_both(smoke, 'Kools', color, 'yellow'):               # 8.
        return False
    if not_both(house_id, 2, drink, 'milk'):                    # 9.
        return False
    if not_both(house_id, 0, nation, 'Norwegian'):              # 10.
        return False
    if not_both(smoke, 'Lucky Strike', drink, 'orange'):        # 13.
        return False
    if not_both(nation, 'Japanese', smoke, 'Parliaments'):      # 14.
        return False
    if not_both(house_id, 1, color, 'blue'):                    # 15 & 10.
        return False
    if color == 'green' and house_id == 0:                      # 6.
        return False
    if color == 'ivory' and house_id == 4:                      # 6.
        return False

    return True


def validate_candidate(candidate):
    # 6.
    for index, tuple_ in candidate.items():
        if tuple_[1] == 'green' and candidate[index-1][1] != 'ivory':
            return False

    def smoke_id(s): return [i for i, t in candidate.items() if t[-1] == s][0]

    if 'fox' not in neighbour_pet(smoke_id("Chesterfields"), candidate):
        return False
    if 'horse' not in neighbour_pet(smoke_id("Kools"), candidate):
        return False

    return True


"""
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
"""


cases = []
for case in product(HOUSE_ID, COLORS, NATIONS, PETS, DRINKS, SMOKES):
    if validate_simple(case):
        cases.append(case)

# print {i: len([c for c in cases if c[0] == i]) for i in range(5)}
# {0: 10, 1: 9, 2: 9, 3: 24, 4: 15}

first = [case for case in cases if case[0] == 0]
second = [case for case in cases if case[0] == 1]
third = [case for case in cases if case[0] == 2]
fourth = [case for case in cases if case[0] == 3]
fifth = [case for case in cases if case[0] == 4]

# 9 choices for 2nd and 3rd house, let's start with that.
combinations = []
for case2 in second:
    for case3 in third:
        if any(case2[i] == case3[i] for i in range(6)):
            # conflict, pray continue
            continue
        used = set(case2[1:] + case3[1:])
        combinations.append({1: case2, 2: case3, -1: used})

# throw in 1st house.
candidates = []
for combination in combinations:
    for case1 in first:
        comb = deepcopy(combination)
        if any(case1[i] in comb[-1] for i in range(6)):
            continue
        comb[-1] = comb[-1] | set(case1[1:])
        comb[0] = case1
        candidates.append(comb)

combinations, candidates = candidates, []

# throw in last house and check with the 4th one.
for combination in combinations:
    for case5 in fifth:
        comb = deepcopy(combination)
        if any(case5[i] in comb[-1] for i in range(6)):
            continue
        all_items = comb[-1] | set(case5[1:])
        for case4 in fourth:
            if any(case4[i] in all_items for i in range(6)):
                continue
            # found a case, this is the only match so we should just add it
            # toe the combination and break it.
            comb[4] = case5
            comb[3] = case4
            del comb[-1]
            candidates.append(comb)
            break

# 168 candidates at this stage, more filter

validated_candidates = []
for candidate in candidates:
    if validate_candidate(candidate):
        validated_candidates.append(candidate)


assert len(validated_candidates) == 1

solution = validated_candidates[0]


def drinks_water():
    return [i[2] for i in solution.values() if i[4] == 'water'][0]


def owns_zebra():
    return [i[2] for i in solution.values() if i[3] == 'zebra'][0]
