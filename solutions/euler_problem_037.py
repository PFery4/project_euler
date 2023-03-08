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
    candidate = 12

    while len(truncatable_primes) != 11:

        # print(candidate)
        if right_truncatable(candidate-1) and left_truncatable(candidate-1):
            truncatable_primes.append(candidate-1)
        if right_truncatable(candidate+1) and left_truncatable(candidate+1):
            truncatable_primes.append(candidate+1)

        candidate += 6

    return sum(truncatable_primes)


if __name__ == "__main__":
    print(solution())
