"""
https://projecteuler.net/problem=47
"""


from utils.prime_numbers import prime_divisors


N = 4                   # the number of consecutive numbers, and the number of distinct prime factors
MAX_LIMIT = 200_000     # the maximum limit of numbers to search


def unique_prime_divisors_up_to(n: int):
    prime_divisors = [0] * (n + 1)

    for i in range(2, n + 1):
        if prime_divisors[i] == 0:
            for j in range(i, n + 1, i):
                prime_divisors[j] += 1

    return prime_divisors


def solution():
    unique_prime_divisors = unique_prime_divisors_up_to(MAX_LIMIT)

    for i in range(644, MAX_LIMIT + 1):
        if all([unique_prime_divisors[j] == N for j in range(i, i + N)]):
            return i


if __name__ == '__main__':
    print(solution())

