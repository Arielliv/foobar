prime_number_10005 = 104779


def solution(i):
    prime_string = concatenate_primes(prime_number_10005)
    return extract_substring(prime_string, i)


def find_all_primes_in_limit(limit):
    primes = []
    prime = [True for _ in range(limit + 1)]
    p = 2
    while p * p <= limit:
        if prime[p] == True:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, limit):
        if prime[p]:
            primes.append(p)
    return primes


def concatenate_primes(limit):
    primes = find_all_primes_in_limit(limit)
    return ''.join(map(str, primes))


def extract_substring(s, start_index):
    return s[start_index:start_index + 5]
