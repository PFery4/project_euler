"""
https://projecteuler.net/problem=12
"""

from utils.find_divisors import find_divisors


def triangle_number(idx: int) -> int:
    return sum(range(idx+1))


def solution():
    num = 1
    triangle_num = triangle_number(num)
    while len(find_divisors(triangle_num)) < 500:
        num += 1
        triangle_num = triangle_number(num)
    return triangle_num


if __name__ == '__main__':
    print(solution())
