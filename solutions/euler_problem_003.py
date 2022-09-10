"""

https://projecteuler.net/problem=3

"""


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def solution():
    target_number = 600851475143

    candidate = 5
    highest_prime = 5

    while candidate < target_number ** 0.5:

        if is_prime(candidate) and target_number % candidate == 0:
            highest_prime = candidate

        candidate += 6

    return highest_prime


if __name__ == '__main__':
    print(solution())
