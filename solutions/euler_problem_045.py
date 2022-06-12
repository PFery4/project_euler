"""

https://projecteuler.net/problem=45

"""


def triangle_number(n):
    return int(n*(n+1)/2)


def pentagonal_number(n):
    return int(n*(3*n-1)/2)


def hexagonal_number(n):
    return int(n*(2*n-1))


if __name__ == '__main__':

    n_h = 143
    n_p = 165
    n_t = 286

    TPN = [triangle_number(n_t), pentagonal_number(n_p), hexagonal_number(n_h)]
    print(TPN)
    print(len(set(TPN)))




