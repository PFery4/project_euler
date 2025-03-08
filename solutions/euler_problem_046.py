"""
https://projecteuler.net/problem=46
"""


from utils.prime_numbers import prime_indices, primes_up_to
from typing import List


MAX_LIMIT = 10_000


def composite_numbers_up_to(n: int) -> List[int]:
    return [k for k, v in enumerate(prime_indices(n)) if not v][2:]


def odd_composites_up_to(n: int) -> List[int]:
    return [v for v in composite_numbers_up_to(n) if v % 2 != 0]


def twice_squares_up_to(n: int) -> List[int]:
    return [2 * v * v for v in range(1, int((n/2)**0.5))]


def solution():

    primes = primes_up_to(MAX_LIMIT)
    odd_composites = odd_composites_up_to(MAX_LIMIT)
    two_squares = twice_squares_up_to(MAX_LIMIT)

    for odd_composite in odd_composites:
        for two_square in two_squares:
            if two_square > odd_composite:
                return odd_composite
            elif odd_composite - two_square in primes:
                break


if __name__ == "__main__":
    print(solution())

