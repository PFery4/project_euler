"""
https://projecteuler.net/problem=27
"""

from utils.prime_numbers import is_prime


def quadratic(a, b, n):
    return n*n + a*n + b


def solution():
    # b must be prime
    b_list = []
    center_candidate = 0
    while center_candidate < 1000:
        if is_prime(center_candidate - 1):
            b_list.append(center_candidate - 1)
        if is_prime(center_candidate + 1):
            b_list.append(center_candidate + 1)
        center_candidate += 6

    longest_streak_consecutive_primes = 0
    ab = 0

    for b in b_list:
        for a in range(-999, 1000):
            n = 0
            while is_prime(quadratic(a, b, n)):
                n += 1

            if n > longest_streak_consecutive_primes:
                longest_streak_consecutive_primes = n
                ab = a * b

    return ab


if __name__ == '__main__':
    print(solution())
