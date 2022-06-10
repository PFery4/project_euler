"""

https://projecteuler.net/problem=10

"""

from euler_problem_3 import is_prime

if __name__ == '__main__':

    big_number = 2_000_000

    primes = [2, 3]

    for i in range(6, big_number, 6):
        if is_prime(i-1):
            primes.append(i-1)
        if is_prime(i+1):
            primes.append(i+1)

    print(sum(primes))

