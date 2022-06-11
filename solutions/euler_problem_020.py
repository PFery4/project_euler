"""

https://projecteuler.net/problem=20

"""

from euler_problem_015 import factorial

if __name__ == '__main__':

    total = 0

    for digit in (str(factorial(100))):
        total += int(digit)

    print(total)
