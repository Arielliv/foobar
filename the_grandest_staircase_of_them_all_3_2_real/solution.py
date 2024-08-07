upper_limit = 202
memoization_table = [[0] * upper_limit for _ in range(upper_limit)]


def solution(n):
    return count_staircase_combinations(1, n) - 1


def count_staircase_combinations(start_height, remaining_bricks):
    if memoization_table[start_height][remaining_bricks] != 0:
        return memoization_table[start_height][remaining_bricks]

    if remaining_bricks == 0:
        return 1
    if remaining_bricks < start_height:
        return 0

    combinations_with_current_height = count_staircase_combinations(start_height + 1, remaining_bricks - start_height)
    combinations_without_current_height = count_staircase_combinations(start_height + 1, remaining_bricks)

    total_combinations = combinations_with_current_height + combinations_without_current_height
    memoization_table[start_height][remaining_bricks] = total_combinations

    return total_combinations
