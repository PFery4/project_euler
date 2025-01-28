"""
https://projecteuler.net/problem=41
"""


from utils.is_prime import is_prime
from itertools import permutations


def solution():    
    p = [int(i) for i in "987654321"]
    while True:
        k = len(p)
        for lst in permutations(p, k):
            candidate = sum([lst[i] * 10 ** (k-1-i) for i in range(k)])
            if is_prime(candidate):
                return candidate
        p.pop(0)


if __name__ == '__main__':
    print(solution())
