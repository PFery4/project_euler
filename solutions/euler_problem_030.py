"""

https://projecteuler.net/problem=30

"""


def sum_fifth_power_digits(n):
    return sum([int(i)**4 for i in str(n)])


if __name__ == '__main__':

    list_sm = []

    i = 2
    sm = sum_fifth_power_digits(i)
    while sm >= i:

        if sm == i:
            list_sm.append(sm)

        sm = sum_fifth_power_digits(i)

        print(i, sm, sm >= i)
        i+=1

    print(sum(list_sm))
