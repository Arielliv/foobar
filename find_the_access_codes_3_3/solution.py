def answer(list_to_check):
    counter = 0
    for first_num_index in range(0, len(list_to_check)):
        nums = findHowAllNumbersInListDiviededByNum(list_to_check, list_to_check[first_num_index])
        for second_num_index in range(0, len(nums)):
            second_nums = findHowAllNumbersInListDiviededByNum(nums, nums[second_num_index])
            counter += len(second_nums)
    return counter


def findHowAllNumbersInListDiviededByNum(list, num_to_check):
    nums = []
    for num in list:
        if num != num_to_check and num % num_to_check == 0:
            nums.append(num)
    return nums
