from typing import List


def find_divisors(n: int) -> List[int]:
    divisors = []
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            divisors.extend([i, n//i])
        i += 1
    return sorted(list(dict.fromkeys(divisors)))
