"""

https://projecteuler.net/problem=5

"""


from math import sqrt, log


# def solution_retired():
#     check_divisible_by = list(range(11, 21))
# 
#     candidate = 2520
# 
#     while not all([candidate % i == 0 for i in check_divisible_by]):
#         candidate += 20
# 
#     return candidate


def solution():
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    k = 20
    N = 1
    i = 0
    a = [0] * k
    check = True
    limit = sqrt(k)
    while p[i] <= k:
        a[i] = 1
        if check:
            if p[i] <= limit:
                a[i] = int(log(k) / log(p[i]))
            else:
                check = False
        N = N * p[i] ** a[i]
        i += 1
    
    return N


if __name__ == '__main__':
    print(solution())
    # print(solution_retired())

