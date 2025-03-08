from typing import List, Set


def find_divisors(n: int) -> List[int]:
    divisors = []
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            divisors.extend([i, n//i])
        i += 1
    return sorted(list(dict.fromkeys(divisors)))

def divisor_set(n: int) -> Set[int]:
    divisors = set()
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            divisors.update({i, n//i})
        i += 1
    return divisors

