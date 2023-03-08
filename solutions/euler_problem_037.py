"""

https://projecteuler.net/problem=37

"""

from euler_problem_003 import is_prime

"""
numbers we are interested in must only contain digits 1, 3, 7 and 9
2, 4, 6, 8, 0 are even and therefore cannot be used to make up a number with the desired property.
5 cannot be used because a number ending with 5 is not prime.
"""


def right_truncatable(number):
    temp_num = str(number)
    rejected = not is_prime(number)
    
    while not rejected and int(temp_num) not in {2, 3, 5, 7}:
        temp_num = temp_num[:-1]
        rejected = not is_prime(int(temp_num))
    
    return not rejected


def left_truncatable(number):
    temp_num = str(number)
    rejected = not is_prime(number)
    
    while not rejected and int(temp_num) not in {2, 3, 5, 7}:
        temp_num = temp_num[1:]
        rejected = not is_prime(int(temp_num))
    
    return not rejected


def solution():

    truncatable_primes = []
    
    # CHANGE STRATEGY, START WITH PRIMES AND ADD PRIMES TO THEIR EDGES
    print(right_truncatable(3797))
    print(left_truncatable(3797))
    return "WIP"


if __name__ == "__main__":
    print(solution())
