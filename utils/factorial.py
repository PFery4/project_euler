
from math import factorial as math_factorial


def recursive_factorial(n: int) -> int:
    return 1 if n<=1 else n * factorial(n - 1)


def iterative_factorial(n: int) -> int:
    product = 1
    for i in range(n, 0, -1):
        product *= i
    return product


factorial = math_factorial

