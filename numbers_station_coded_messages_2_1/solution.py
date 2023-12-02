# o(n^2)
# def answer(l, t):
#     for i in range(0, len(l)):
#         count = t
#         for j in range(i, len(l)):
#             count = count - l[j]
#             if count == 0:
#                 return [i, j]
#             if count < 0:
#                 break
#     return [-1, -1]

# o(n)
def answer(l, t):
    start_index, end_index = 0, 0
    current_sum = 0

    for end_index in range(len(l)):
        current_sum += l[end_index]

        while current_sum > t:
            current_sum -= l[start_index]
            start_index += 1

        if current_sum == t:
            return [start_index, end_index]

    return [-1, -1]
