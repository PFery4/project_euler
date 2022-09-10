"""

https://projecteuler.net/problem=28

"""


def solution():
    in_diag = [1]

    edge_length = 2
    n = 1

    while edge_length < 1001:
        for i in range(4):
            n += edge_length
            in_diag.append(n)
        edge_length += 2

    return sum(in_diag)


if __name__ == '__main__':
    print(solution())
