"""
https://projecteuler.net/problem=23
"""

from itertools import combinations_with_replacement
from utils.find_divisors import divisor_set


def is_abundant(n: int) -> bool:
    return sum(divisor_set(n)) > 2 * n


def solution():
    abundants = {i for i in range(1, 28124) if is_abundant(i)}
    sum_2_abundants = {sum(pair) for pair in combinations_with_replacement(abundants, 2)}
    non_sum_2_abundants = {i for i in range(1, 28124) if i not in sum_2_abundants}
    return sum(non_sum_2_abundants)


if __name__ == '__main__':
    print(solution())

