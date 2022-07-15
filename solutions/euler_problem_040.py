"""

https://projecteuler.net/problem=40

"""


def main():
    integer = 0
    decimal = "0."

    while len(decimal) < 1_000_002:  # accounting for the 2 characters at start: '0.'
        integer += 1
        decimal += str(integer)

    result = 1
    for i in range(7):
        result *= int(decimal[10 ** i + 1])  # again, accounting for the characters at start

    return result


if __name__ == '__main__':
    print(main())
