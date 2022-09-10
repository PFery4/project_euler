"""

https://projecteuler.net/problem=29

"""


def solution():
    the_list = []

    for a in range(2, 101):
        for b in range(2, 101):
            the_list.append(a ** b)

    return len(list(dict.fromkeys(the_list)))


if __name__ == '__main__':
    print(solution())
