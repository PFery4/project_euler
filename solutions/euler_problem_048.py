"""

https://projecteuler.net/problem=48

"""


def solution():
    return str(sum([i**i for i in range(1, 1001)]))[-10:]


if __name__ == '__main__':
    print(solution())
