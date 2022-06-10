"""

https://projecteuler.net/problem=7

"""

from euler_problem_3 import is_prime

if __name__ == '__main__':

    primes_list = [2, 3]

    center_candidate = 0            # primes are 1 apart from center_candidate

    while len(primes_list) < 10001:

        if is_prime(center_candidate - 1):
            primes_list.append(center_candidate - 1)

        if is_prime(center_candidate + 1):
            primes_list.append(center_candidate + 1)

        center_candidate += 6

    print(primes_list[-1])
