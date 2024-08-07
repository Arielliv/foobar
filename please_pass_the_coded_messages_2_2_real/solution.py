def solution(l):
    largest_divisible_group_by_3_result = largest_divisible_group_by_3(l)
    if len(largest_divisible_group_by_3_result) == 0:
        return 0
    else:
        largest_divisible_group_by_3_result.sort(reverse=True)
        return concat_numbers(largest_divisible_group_by_3_result)


def largest_divisible_group_by_3(list_of_numbers):
    remainder_groups = {0: [], 1: [], 2: []}
    for digit in list_of_numbers:
        remainder_groups[digit % 3].append(digit)

    total_sum = sum(list_of_numbers)
    remainder = total_sum % 3

    def remove_smallest(group, count):
        group.sort()
        for _ in range(count):
            if group:
                group.pop(0)

    if remainder == 1:
        if remainder_groups[1]:
            remove_smallest(remainder_groups[1], 1)
        else:
            remove_smallest(remainder_groups[2], 2)
    elif remainder == 2:
        if remainder_groups[2]:
            remove_smallest(remainder_groups[2], 1)
        else:
            remove_smallest(remainder_groups[1], 2)

    result = remainder_groups[0] + remainder_groups[1] + remainder_groups[2]
    return result


def concat_numbers(numbers_list):
    concatenated_str = ''.join(map(str, numbers_list))
    return int(concatenated_str)
