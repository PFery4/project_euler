"""

https://projecteuler.net/problem=38

"""


def concat_product(k, n):
    """
    example:
        - k = 192
        - n = 3

        out = 192*1 , 192*2, 192*3 concatenated --> 192384576
    """
    out = ""
    for i in range(1, n+1):
        out += str(i*k)
    return int(out)


def is_pandigit(n):
    return len(str(n)) == 9 and all([str(i) in str(n) for i in range(1, 10)])


def solution():
    print(concat_product(192, 3))
    print(is_pandigit(concat_product(192, 3)))
    pandigits = []

    for n in range(2, 10):
        pandigit_found = False
        candidate_k = 1
        while not pandigit_found:
            proposal = concat_product(candidate_k, n)
            if is_pandigit(proposal):
                pandigits.append(proposal)
            candidate_k += 1

        print(n)

    return "WIP"


if __name__ == "__main__":
    print(solution())