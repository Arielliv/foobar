import numpy as np
from fractions import Fraction

def calculate_lcm(list_x):
    greater = max(list_x)
    while not all(greater % x == 0 for x in list_x):
        greater += 1
    return greater

def matrix_inverse(m):
    size_m = len(m)
    diag = np.identity(size_m)

    for i in range(size_m):
        diag[i] = [mi / m[i][i] for mi in diag[i]]
        m[i] = [mi / m[i][i] for mi in m[i]]

        for j in range(i + 1, size_m):
            ratio = m[j][i] / m[i][i]
            m[j] = [m[j][k] - m[i][k] * ratio for k in range(size_m)]
            diag[j] = [diag[j][k] - diag[i][k] * ratio for k in range(size_m)]

    for i in range(size_m - 1, -1, -1):
        diag[i] = [mi / m[i][i] for mi in diag[i]]
        m[i] = [mi / m[i][i] for mi in m[i]]

        for j in range(i - 1, -1, -1):
            ratio = m[j][i] / m[i][i]
            m[j] = [m[j][k] - m[i][k] * ratio for k in range(size_m)]
            diag[j] = [diag[j][k] - diag[i][k] * ratio for k in range(size_m)]

    return diag

def answer(m):
    if sum(m[0]) == 0:
        return [1, 1]

    m_np = np.array(m)
    size_m = len(m_np)

    index_non_zero = [i for i in range(size_m) if sum(m_np[i]) != 0]
    index_zeros = [i for i in range(size_m) if sum(m_np[i]) == 0]

    m_np = np.array([[float(ir) / sum(r) for ir in r] if sum(r) != 0 else [0] * size_m for r in m_np])

    if not index_zeros:
        m_prob = m_np
        for _ in range(100):
            m_prob = np.matmul(m_prob, m_np)
        m_fr = m_prob
    else:
        m_q = np.array([r[index_non_zero] for r in m_np[index_non_zero]])
        m_I = np.identity(len(m_q))
        m_f = np.linalg.inv(m_I - m_q)
        m_r = np.array([r[index_zeros] for r in m_np[index_non_zero]])

        m_fr = np.matmul(m_f, m_r)

    m_fr = m_fr[0, :]
    m_fr = np.array([Fraction(i).limit_denominator() for i in m_fr])

    lcm = np.lcm.reduce([m.denominator for m in m_fr])
    m_fr_norm = m_fr * lcm

    return [int(i) for i in m_fr_norm] + [lcm]
