"""

https://projecteuler.net/problem=26

"""


def decimal_representation(n, d):
    div, remainder = divmod(n, d)
    first_div = str(div) + '.'

    decimals = ''
    remainders = [remainder]
    index = None

    while remainder != 0:
        remainder *= 10
        div, remainder = divmod(remainder, d)
        decimals += str(div)
        if remainder in remainders:
            index = remainders.index(remainder)
            break
        remainders.append(remainder)

    if index is not None:
        decimals = decimals[:index] + "(" + decimals[index:] + ")"

    return first_div + decimals


def length_repeat(decimal_rep):
    if "(" not in decimal_rep:
        return 0
    return len(decimal_rep) - decimal_rep.index('(') - 2


def solution():
    value_of_d = 0
    longest_repeat = 0

    for d in range(1, 1000):
        decimal = decimal_representation(1, d)
        if length_repeat(decimal) > longest_repeat:
            longest_repeat = length_repeat(decimal)
            value_of_d = d

    return value_of_d


if __name__ == '__main__':
    print(solution())
