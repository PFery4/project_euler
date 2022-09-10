"""

https://projecteuler.net/problem=2

"""


def solution():
    sum_even_fibonacci = 2

    fibo_prev = 1
    fibo_current = 2

    while fibo_current < 4_000_000:

        fibo_next = fibo_prev + fibo_current

        fibo_prev = fibo_current
        fibo_current = fibo_next

        if fibo_next % 2 == 0:
            sum_even_fibonacci += fibo_next

    return sum_even_fibonacci


if __name__ == '__main__':
    print(solution())
