"""
https://projecteuler.net/problem=44
"""


def penta_n(n: int) -> int:
    return n * (3 * n - 1) // 2


def solution():
    x = 1
    pentagonals = [penta_n(1)]
    
    while True:
        x += 1
        pentagonals.append(penta_n(x))

        j_index = 0
        D = pentagonals[-1] - 2 * pentagonals[j_index]

        while D > 0:
            if D in pentagonals and pentagonals[j_index] + D in pentagonals[j_index:]:
               return D

            j_index += 1
            D = pentagonals[-1] - 2 * pentagonals[j_index]


if __name__ == '__main__':
    print(solution())

