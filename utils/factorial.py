
def factorial(n: int) -> int:
    product = 1
    for i in range(n, 0, -1):
        product *= i
    return product
