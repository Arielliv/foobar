def solution(l):
    total_triples = 0
    divisor_count = [0] * len(l)

    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                divisor_count[i] += 1
                total_triples += divisor_count[j]

    return total_triples
