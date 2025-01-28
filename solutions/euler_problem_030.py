"""
https://projecteuler.net/problem=30
"""


def sum_power_digits(n, exp=5):
    return sum([int(i)**exp for i in str(n)])


def solution():
    nums = []
    # stopping condition is set to 1000000 because sum_power_digits(999999) < 999999
    for i in range(10, 1000000):
        if i == sum_power_digits(i):
            nums.append(i)
    return sum(nums)


if __name__ == '__main__':
    print(solution())
