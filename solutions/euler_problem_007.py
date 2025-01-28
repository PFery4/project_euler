"""
https://projecteuler.net/problem=7
"""

from utils.is_prime import is_prime


def solution():
    primes_list = [2, 3]
    center_candidate = 0  # primes are 1 apart from center_candidate

    while len(primes_list) < 10001:

        if is_prime(center_candidate - 1):
            primes_list.append(center_candidate - 1)

        if is_prime(center_candidate + 1):
            primes_list.append(center_candidate + 1)

        center_candidate += 6

    return primes_list[-1]


if __name__ == '__main__':
    print(solution())
