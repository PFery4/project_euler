"""

https://projecteuler.net/problem=26

"""


def decimal_representation(n, d):
    div, remainder = divmod(n, d)

    first_div = str(div) + '.'

    decimals = ''
    index = None

    while remainder != 0:
        remainder *= 10
        while remainder < d:
            remainder *= 10
            decimals += '0'
        div, remainder = divmod(remainder, d)
        if str(div) in decimals:
            index = decimals.index(str(div))
            break
        decimals += str(div)

    if index is not None:
        decimals = decimals[:index] + "(" + decimals[index:] + ")"

    return first_div + decimals


if __name__ == '__main__':

    for i in range(1,500):
        print(decimal_representation(1, i))

