"""

https://projecteuler.net/problem=35

"""

from euler_problem_003 import is_prime

def solution():

    circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]
    
    # circular primes can only be made up of 1, 3, 7, and 9 from here on out
    useful_integers = [1, 3, 7, 9]
    
    prime_candidates = []
    
    print(is_prime(2))
    print(is_prime(15))
    
    for i in range(3, 4):   # replace 4 with 7 down the road
        print(i)
        number = 0
        for decimal_place in range(i):
            print(10**decimal_place)
    
    return "WIP"    # len(circular_primes)


if __name__ == '__main__':
    print(solution())
