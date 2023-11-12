import math


def is_even(num):
    return num % 2 == 0


def answer(num):
    int_num = int(num)
    res = [None] * (int_num + 2)
    res[1] = 0
    return solve(int_num, res)


def solve(int_num, data):
    if int_num == 1:
        return 0

    for current_num in range(2, int_num + 1):
        if is_even(current_num):
            data[current_num] = data[math.floor(current_num / 2)] + 1
        else:
            data[current_num] = min((data[math.floor((current_num + 1) / 2)] + 1), data[current_num - 1]) + 1

    return data[int_num]
