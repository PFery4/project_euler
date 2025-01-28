"""
https://projecteuler.net/problem=9
"""


def is_pythagorean_triplet(a, b, c):
    return a * a + b * b == c * c


def solution():
    a = 1
    b = 2
    c = 997

    while not is_pythagorean_triplet(a, b, c):

        c -= 1
        ab = 1000 - c

        for a in range(1, ab):

            b = ab - a

            if b <= a:
                continue

            if is_pythagorean_triplet(a, b, c):
                break

    return a * b * c


if __name__ == '__main__':
    print(solution())
