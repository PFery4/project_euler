"""
https://projecteuler.net/problem=37
"""

from utils.is_prime import is_prime


def is_right_truncatable(number: int) -> bool:
    temp_num = str(number)
    rejected = not is_prime(number)
    
    while not rejected and int(temp_num) not in {2, 3, 5, 7}:
        temp_num = temp_num[:-1]
        rejected = not is_prime(int(temp_num))
    return not rejected


def is_left_truncatable(number: int) -> bool:
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
        if is_right_truncatable(candidate-1) and is_left_truncatable(candidate-1):
            truncatable_primes.append(candidate-1)
        if is_right_truncatable(candidate+1) and is_left_truncatable(candidate+1):
            truncatable_primes.append(candidate+1)
        candidate += 6
    return sum(truncatable_primes)


if __name__ == "__main__":
    print(solution())
