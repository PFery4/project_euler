"""

https://projecteuler.net/problem=23

"""

from euler_problem_012 import find_divisors


def is_abundant(n):
    divisors = find_divisors(n)
    return sum(divisors[:-1]) > n


if __name__ == '__main__':

    abundants = []

    for i in range(1, 28124):
        if is_abundant(i):
            abundants.append(i)

    sum_2_abundants = []

    for i in abundants:
        for j in abundants:
            sum_2_abundants.append(i + j)

    sum_2_abundants = sorted(list(dict.fromkeys(sum_2_abundants)))

    non_sum_2_abundants = []

    for i in range(1, 28124):
        if i not in sum_2_abundants:
            non_sum_2_abundants.append(i)

    print(sum(non_sum_2_abundants))
