"""
https://projecteuler.net/problem=20
"""

from utils.factorial import factorial


def solution():
    total = 0
    for digit in (str(factorial(100))):
        total += int(digit)
    return total


if __name__ == '__main__':
    print(solution())
