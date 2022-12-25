"""

https://projecteuler.net/problem=37

"""

from euler_problem_003 import is_prime


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
    
    return "WIP"

if __name__ == "__main__":
    print(solution())
