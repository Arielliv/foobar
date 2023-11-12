import math

Impossible = "impossible"

been_path = {}


def answer(mach_num, facula_num):
    res = bombs_count_recursive(0, 1, 1, int(mach_num), int(facula_num))
    # res2 = dynamic(create_matrix(mach_num + 1, facula_num + 1), mach_num, facula_num)
    res3 = bombs_count_dynamic(mach_num, facula_num)
    print(res3)
    if res == None:
        return Impossible
    else:
        return res


def bombs_count_recursive(lvl, cur_mach_count, cur_facula_count, mach_num_boundary, facula_num_boundary):
    key = f"{cur_mach_count}-{cur_facula_count}"
    # print(key, lvl)
    if key in been_path or cur_mach_count == 0 and cur_facula_count == 0:
        return None
    elif mach_num_boundary < cur_mach_count or facula_num_boundary < cur_facula_count:
        return None
    elif cur_mach_count == mach_num_boundary and cur_facula_count == facula_num_boundary:
        return lvl
    else:
        been_path[key] = True
        lvl += 1

        return bombs_count_recursive(lvl, cur_mach_count + cur_facula_count, cur_facula_count, mach_num_boundary,
                                     facula_num_boundary) or bombs_count_recursive(lvl, cur_mach_count,
                                                                                   cur_mach_count + cur_facula_count,
                                                                                   mach_num_boundary,
                                                                                   facula_num_boundary)


# def create_matrix(m, n):
#     if m <= 0 or n <= 0:
#         return []
#
#     matrix = [[None] * n for _ in range(m)]
#     return matrix
#
# def dynamic(matrix, mach_num_boundary, facula_num_boundary):
#     matrix[0][0] = 0
#     matrix[0][1] = 0
#     matrix[1][0] = 0
#     matrix[1][1] = 0
#     for i in range(1, mach_num_boundary + 1):
#         for j in range(1, facula_num_boundary + 1):
#             if (i - 1 + j - 1) >= mach_num_boundary + 1 or (i - 1 + j - 1) >= facula_num_boundary + 1 or (
#                     i - 1 + j - 1) < 0 or (i - 1) < 0 or (j - 1) < 0:
#                 continue
#             if matrix[i - 1 + j - 1][j - 1] is None and matrix[i - 1][j - 1 + i - 1] is None:
#                 matrix[i][j] = None
#             else:
#                 if i == 3 and j == 2:
#                     print(matrix[i - 1 + j - 1][j - 1], matrix[i - 1][j - 1 + i - 1])
#                 matrix[i][j] = (matrix[i - 1 + j - 1][j - 1] or matrix[i - 1][j - 1 + i - 1]) + 1
#                 print(i, j, matrix[i][j])
#     return matrix[mach_num_boundary][facula_num_boundary]


def bombs_count_dynamic(M, F):
    M = int(M)
    F = int(F)
    counter = 0

    print("{M:" + str(M) + ", F:" + str(F) + "}")

    while (M > 1 or F > 1):
        if (M % 2 == 0 and F % 2 == 0) or M < 1 or F < 1:
            return "impossible"
        if (M > F):
            counter += math.floor(M / F)
            M %= F
        else:
            counter += math.floor(F / M)
            F %= M

        if (M == 0 or F == 0):  # is 1 step more than start point 1,1
            counter -= 1

        print("#" + str(counter) + ". {M:" + str(M) + ", F:" + str(F) + "}")

    return str(counter)
