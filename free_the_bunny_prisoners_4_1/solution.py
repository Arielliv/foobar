from itertools import combinations

def answer(num_buns, num_required):
    # If no keys are required, return an empty list
    if num_required == 0:
        return [[]] if num_buns > 0 else []

    # Initialize the list of keys assigned to each bunny
    keys_assigned = [[] for _ in range(num_buns)]

    # Generate combinations of bunnies
    bunny_combinations = list(combinations(range(num_buns), num_buns - num_required + 1))

    # Assign keys to bunnies based on combinations
    for key_count, combination in enumerate(bunny_combinations):

        for bunny in combination:
            keys_assigned[bunny].append(key_count)

    return keys_assigned