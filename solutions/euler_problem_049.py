"""
https://projecteuler.net/problem=49
"""

from itertools import combinations, combinations_with_replacement, permutations
from utils.prime_numbers import is_prime


def solution():

    for comb in combinations_with_replacement(range(1, 10), 4):

        if comb == (1, 4, 7, 8):
            continue

        primes = []
        for perm in permutations(comb):
            if len({*perm}) == 1:
                break
            num = sum([x * 10 ** e for x, e in zip(perm, range(3, -1, -1))])
            if is_prime(num):
                primes.append(num)
        primes = list(dict.fromkeys(primes))

        if len(primes) > 2:
            for prime_comb in combinations(primes, 3):
                if prime_comb[2] - prime_comb[1] == prime_comb[1] - prime_comb[0]:
                   return sum([x * 10 ** a for x, a in zip(prime_comb, range(8, -1, -4))])

if __name__ == '__main__':
    print(solution())

