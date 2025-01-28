"""
https://projecteuler.net/problem=21
"""

from typing import Set, Tuple


def sum_factors(n: int) -> int:
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.extend([i, n // i])
    return sum(set(result) - set([n]))


def amicable_pair(number: int) -> Set[Tuple[int, int]]:
    result = []
    for x in range(1, number + 1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result.append(tuple(sorted((x, y))))
    return set(result)


def solution():
    allpairs = amicable_pair(10000)
    total = 0
    for tupl in allpairs:
        total += sum(tupl)
    return total


if __name__ == '__main__':
    print(solution())
