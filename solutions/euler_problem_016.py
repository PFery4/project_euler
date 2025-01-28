"""
https://projecteuler.net/problem=16
"""


def solution():
    return sum([int(element) for element in str(2**1000)])


if __name__ == '__main__':
    print(solution())
