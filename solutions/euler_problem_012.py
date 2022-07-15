"""

https://projecteuler.net/problem=12

"""


def triangle_number(idx):
    return sum(range(idx+1))


def find_divisors(n):
    divisors = []
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            divisors.extend([i, n//i])
        i += 1
    return sorted(list(dict.fromkeys(divisors)))


def main():
    num = 1
    triang = triangle_number(num)
    while len(find_divisors(triang)) < 500:
        num += 1
        triang = triangle_number(num)

    return triang


if __name__ == '__main__':
    print(main())
