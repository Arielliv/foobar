def answer(data, n):
    minion_occurrence_map = {}
    result = []
    for i in data:
        if i not in minion_occurrence_map:
            minion_occurrence_map[i] = 1
        else:
            minion_occurrence_map[i] += 1

    for i in data:
        if minion_occurrence_map[i] <= n:
            result.append(i)

    return result
