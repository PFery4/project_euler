"""

https://projecteuler.net/problem=45

"""


def triangle_number(n):
    return int(n*(n+1)/2)


def pentagonal_number(n):
    return int(n*(3*n-1)/2)


def hexagonal_number(n):
    return int(n*(2*n-1))


def solution():
    n_t = 285
    n_p = 165
    n_h = 144

    T = triangle_number(n_t)
    P = pentagonal_number(n_p)
    H = hexagonal_number(n_h)

    while len({T, P, H}) != 1:
        while len({P, H}) != 1:
            if P < H:
                n_p += 1
                P = pentagonal_number(n_p)
            elif H < P:
                n_h += 1
                H = hexagonal_number(n_h)
        if T < P:
            n_t += 1
            T = triangle_number(n_t)
        elif P < T:
            n_p += 1
            P = pentagonal_number(n_p)

    assert T == P == H

    return T


if __name__ == '__main__':
    print(solution())
