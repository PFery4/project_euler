"""

https://projecteuler.net/problem=12

"""


def triangle_number(idx):
    return sum(range(idx+1))


def find_divisors(n):
    divisors = [1, n]

    if n % 2 == 0:
        divisors.extend([2, n//2])
    for i in range(3, n//3+1, 2):
        if n % i == 0:
            divisors.extend([i, n//i])

    return list(dict.fromkeys(sorted(divisors)))


if __name__ == '__main__':

    divisor_list = []
    i = 0

    while len(divisor_list) < 500:
        i += 500
        triang = triangle_number(i)
        divisor_list = find_divisors(triang)
        print(i, triang, len(divisor_list))

    print(divisor_list)
