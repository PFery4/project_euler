"""

https://projecteuler.net/problem=26

"""


def long_division(n, d):
    decimals = []
    already_seen = []

    div, remainder = divmod(n, d)
    decimals.append(str(div))

    while remainder != 0 and div not in already_seen[:-1]:
        remainder *= 10
        div, remainder = divmod(remainder, d)
        if div in already_seen[:-1]:
            break
        else:
            already_seen.append(div)
            decimals.append(str(div))

    return decimals


if __name__ == '__main__':

    print(long_division(1, 7))
