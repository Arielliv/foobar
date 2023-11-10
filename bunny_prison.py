from itertools import combinations
from math import factorial


def answer(num_buns, num_required):
    res = []

    if num_required == 1:
        for i in range(0, num_buns):
            res.append([0])
        return res

    if num_buns == num_required:
        for i in range(0, num_buns):
            res.append([i])
        return res

    if num_buns > num_required:
        res = generate_key_distribution(num_buns, num_required)
        for i, keys in enumerate(res):
            print(f"Bunny {i}: {keys}")
    return res


def generate_key_distribution(num_buns, num_required):
    if num_required == 0:
        return [[]] if num_buns > 0 else []

    # Initialize the list of keys assigned to each bunny
    keys_assigned = [[] for _ in range(num_buns)]

    # Initialize the list of keys
    keys = list(range(num_buns))

    # Generate combinations of keys
    key_combinations = list(combinations(keys, num_required))

    # Assign keys to bunnies based on combinations
    for i, combination in enumerate(key_combinations):
        for key in combination:
            keys_assigned[key].append(i)

    return keys_assigned
