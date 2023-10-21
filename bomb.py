Impossible = "impossible"

been_path = {}


def answer(mach_num, facula_num):
    res = bombs_count_recursive(0, 1, 1, mach_num, facula_num)
    if res == None:
        return Impossible
    else:
        return res


def bombs_count_recursive(lvl, cur_mach_count, cur_facula_count, mach_num_boundary, facula_num_boundary):
    key = f"{cur_mach_count}-{cur_facula_count}"
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

# def dynamic(lvl, cur_mach_count, cur_facula_count, mach_num_boundary, facula_num_boundary):
#     for m in range(0, mach_num_boundary):
#         for f in range(0, facula_num_boundary):
#
#     key = f"{cur_mach_count}-{cur_facula_count}"
#     if key in been_path or cur_mach_count == 0 and cur_facula_count == 0:
#         return None
#     elif mach_num_boundary < cur_mach_count or facula_num_boundary < cur_facula_count:
#         return None
#     elif cur_mach_count == mach_num_boundary and cur_facula_count == facula_num_boundary:
#         return lvl
#     else:
#         been_path[key] = True
#         lvl += 1
#
#         return bombs_count_recursive(lvl, cur_mach_count + cur_facula_count, cur_facula_count, mach_num_boundary,
#                                      facula_num_boundary) or bombs_count_recursive(lvl, cur_mach_count,
#                                                                                    cur_mach_count + cur_facula_count,
#                                                                                    mach_num_boundary,
#                                                                                    facula_num_boundary)
