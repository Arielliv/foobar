import numpy as np
from fractions import Fraction


def solution(transition_matrix):
    if sum(transition_matrix[0]) == 0:
        return [1, 1]

    transition_matrix_np = np.array(transition_matrix)
    num_states = len(transition_matrix_np)

    non_terminal_states = [i for i in range(num_states) if sum(transition_matrix_np[i]) != 0]
    terminal_states = [i for i in range(num_states) if sum(transition_matrix_np[i]) == 0]

    probability_matrix = np.array([[float(entry) / sum(row) for entry in row]
                                   if sum(row) != 0 else [0] * num_states for row in transition_matrix_np])

    if not terminal_states:
        steady_state_matrix = probability_matrix
        for _ in range(100):
            steady_state_matrix = np.matmul(steady_state_matrix, probability_matrix)
        final_probabilities = steady_state_matrix
    else:
        transition_matrix_q = np.array([row[non_terminal_states] for row in probability_matrix[non_terminal_states]])
        identity_matrix = np.identity(len(transition_matrix_q))
        fundamental_matrix = np.linalg.inv(identity_matrix - transition_matrix_q)
        transition_matrix_r = np.array([row[terminal_states] for row in probability_matrix[non_terminal_states]])

        final_probabilities = np.matmul(fundamental_matrix, transition_matrix_r)

    terminal_state_probabilities = final_probabilities[0, :]
    terminal_state_fractions = np.array(
        [Fraction(probability).limit_denominator() for probability in terminal_state_probabilities])

    lcm_common_denominator = np.lcm.reduce([fraction.denominator for fraction in terminal_state_fractions])
    normalized_probabilities = terminal_state_fractions * lcm_common_denominator

    return [int(probability) for probability in normalized_probabilities] + [lcm_common_denominator]


def calculate_lcm(numbers_list):
    greatest_number = max(numbers_list)
    while not all(greatest_number % number == 0 for number in numbers_list):
        greatest_number += 1
    return greatest_number


def matrix_inverse(matrix):
    matrix_size = len(matrix)
    identity_matrix = np.identity(matrix_size)

    for i in range(matrix_size):
        identity_matrix[i] = [identity_entry / matrix[i][i] for identity_entry in identity_matrix[i]]
        matrix[i] = [matrix_entry / matrix[i][i] for matrix_entry in matrix[i]]

        for j in range(i + 1, matrix_size):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix_entry - matrix[i][k] * factor for k, matrix_entry in enumerate(matrix[j])]
            identity_matrix[j] = [identity_entry - identity_matrix[i][k] * factor for k, identity_entry in
                                  enumerate(identity_matrix[j])]

    for i in range(matrix_size - 1, -1, -1):
        identity_matrix[i] = [identity_entry / matrix[i][i] for identity_entry in identity_matrix[i]]
        matrix[i] = [matrix_entry / matrix[i][i] for matrix_entry in matrix[i]]

        for j in range(i - 1, -1, -1):
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix_entry - matrix[i][k] * factor for k, matrix_entry in enumerate(matrix[j])]
            identity_matrix[j] = [identity_entry - identity_matrix[i][k] * factor for k, identity_entry in
                                  enumerate(identity_matrix[j])]

    return identity_matrix
