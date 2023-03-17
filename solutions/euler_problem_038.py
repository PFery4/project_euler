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
    pandigits = []

    candidate_k = 1
    candidate_n = 2
    
    proposal = concat_product(candidate_k, candidate_n)
    
    while candidate_n < 10:
        while len(str(proposal)) < 10:
            
            # print(candidate_k, candidate_n)
            
            candidate_k += 1
            proposal = concat_product(candidate_k, candidate_n)
            if is_pandigit(proposal):
                pandigits.append(proposal)
        candidate_n += 1
            
    # print(pandigits)

    return max(pandigits)


if __name__ == "__main__":
    print(solution())

