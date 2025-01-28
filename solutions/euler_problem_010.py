"""
https://projecteuler.net/problem=10
"""

from utils.is_prime import is_prime


def solution():
    primes = [2, 3]

    for i in range(6, 2_000_000, 6):

        if is_prime(i - 1):
            primes.append(i - 1)

        if is_prime(i + 1):
            primes.append(i + 1)

    return sum(primes)


if __name__ == '__main__':
    print(solution())
