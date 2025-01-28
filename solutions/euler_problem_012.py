"""
https://projecteuler.net/problem=12
"""

from typing import List


def triangle_number(idx: int) -> int:
    return sum(range(idx+1))


def find_divisors(n: int) -> List[int]:
    divisors = []
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            divisors.extend([i, n//i])
        i += 1
    return sorted(list(dict.fromkeys(divisors)))


def solution():
    num = 1
    triangle_num = triangle_number(num)
    while len(find_divisors(triangle_num)) < 500:
        num += 1
        triangle_num = triangle_number(num)
    return triangle_num


if __name__ == '__main__':
    print(solution())
