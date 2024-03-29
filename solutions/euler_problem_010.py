"""

https://projecteuler.net/problem=10

"""

from euler_problem_003 import is_prime


def solution():
    big_number = 2_000_000

    primes = [2, 3]

    for i in range(6, big_number, 6):

        if is_prime(i - 1):
            primes.append(i - 1)

        if is_prime(i + 1):
            primes.append(i + 1)

    return sum(primes)


if __name__ == '__main__':
    print(solution())
