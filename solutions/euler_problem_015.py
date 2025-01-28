"""
https://projecteuler.net/problem=15
"""

from utils.factorial import factorial


def n_choose_k(n: int, k: int) -> int:
    return (factorial(n)) // (factorial(k) * factorial(n-k))


def solution():
    # equivalent to the number of possible sequences of 40 coin tosses with exactly 20 heads and 20 tails
    return int(n_choose_k(40, 20))


if __name__ == '__main__':
    print(solution())

