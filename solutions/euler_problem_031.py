"""

https://projecteuler.net/problem=31

"""


def main():
    currency_elements = [1, 2, 5, 10, 20, 50, 100, 200]  # in unit pence, [p]

    total = 200

    ways = [0] * (total + 1)
    ways[0] = 1

    for x in currency_elements:
        for i in range(x, total + 1):
            ways[i] += ways[i - x]

    return ways[-1]


if __name__ == '__main__':
    print(main())
