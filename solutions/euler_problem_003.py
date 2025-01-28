"""
https://projecteuler.net/problem=3
"""

from utils.is_prime import is_prime

TARGET = 600851475143


def solution():

    candidate = 5
    highest_prime = 5

    while candidate < TARGET ** 0.5:

        if is_prime(candidate) and TARGET % candidate == 0:
            highest_prime = candidate

        candidate += 6

    return highest_prime


if __name__ == '__main__':
    print(solution())
