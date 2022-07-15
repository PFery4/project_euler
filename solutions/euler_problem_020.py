"""

https://projecteuler.net/problem=20

"""

from euler_problem_015 import factorial


def main():
    total = 0

    for digit in (str(factorial(100))):
        total += int(digit)

    return total


if __name__ == '__main__':
    print(main())
