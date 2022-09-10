"""

https://projecteuler.net/problem=6

"""


def solution():
    sum_of_squares = 0

    for i in range(101):
        sum_of_squares += i * i

    return (50 * 101) ** 2 - sum_of_squares


if __name__ == '__main__':
    print(solution())
