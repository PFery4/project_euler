"""

https://projecteuler.net/problem=35

"""

from euler_problem_003 import is_prime


def cycle(number):
    """
    provides the next cycle of a number
    
    123 -> 231
    """
    return int(str(number)[1:] + str(number)[0])

def solution():

    circular_primes = [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]

    # circular primes can only be made up of 1, 3, 7, and 9 from here on out
    useful_integers = [1, 3, 7, 9]

    prime_candidates = []

    for candidate in range(100, 1000000): # replace with 1million
    
        if candidate % 10 not in useful_integers or "0" in str(candidate):
            continue
        # print(candidate)
        
        rejected = not is_prime(candidate)
        cycles = []
        shift = candidate

        while len(cycles) != len(str(candidate)) and not rejected:
            shift = cycle(shift)
            if is_prime(shift):
                cycles.append(shift)
            else:
                rejected = True
        
        if len(cycles) == len(str(candidate)):
            circular_primes.extend(cycles)
    
    circular_primes = sorted(list(set(circular_primes)))

    # print(circular_primes)
    return len(circular_primes)


if __name__ == '__main__':
    print(solution())
