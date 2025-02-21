from typing import List


def prime_indices(n: int) -> List[bool]:
    # generates a list of booleans, where each element indicates whether its corresponding index number i is prime or not.
    # starts at 0
    # uses the sieve of Eratosthenes.

    prime_indices = [True] * (n + 1)
    prime_indices[:2] = False, False

    for i in range(2, n + 1):
        if prime_indices[i]:
            for j in range(2 * i, n + 1, i):
                prime_indices[j] = False

    return prime_indices


def primes_up_to(n: int) -> List[int]:
   return [k for k, v in enumerate(prime_indices(n)) if v]


def is_prime(n: int) -> bool:
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


def prime_divisors(n: int) -> List[int]:

    primes_to_check = primes_up_to(n)

    if primes_to_check[-1] == n:
        return [n]

    prime_divs = []

    while n != 1:
        for prime in primes_to_check:
            if n % prime == 0:
                prime_divs.append(prime)
                n /= prime
                break

    return prime_divs


def primes_generator():
    yield 2
    yield 3

    i = 6
    while True:

        imin = i - 1
        if is_prime(imin):
            yield imin

        iplus = i + 1
        if is_prime(iplus):
            yield iplus

        i += 6

