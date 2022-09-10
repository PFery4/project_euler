"""

https://projecteuler.net/problem=15

"""


def factorial(n):
    product = 1
    for i in range(n, 0, -1):
        product *= i
    return product


def n_choose_k(n, k):
    return (factorial(n)) / (factorial(k) * factorial(n-k))


def solution():
    # equivalent to the number of possible sequences of 40 coin tosses with exactly 20 heads and 20 tails
    return int(n_choose_k(40, 20))


if __name__ == '__main__':
    print(solution())

