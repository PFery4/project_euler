"""
https://projecteuler.net/problem=5
"""


from math import sqrt, log

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def solution():
    k = 20
    N = 1
    i = 0
    a = [0] * k
    check = True
    limit = sqrt(k)
    while PRIMES[i] <= k:
        a[i] = 1
        if check:
            if PRIMES[i] <= limit:
                a[i] = int(log(k) / log(PRIMES[i]))
            else:
                check = False
        N = N * PRIMES[i] ** a[i]
        i += 1
    
    return N


if __name__ == '__main__':
    print(solution())
