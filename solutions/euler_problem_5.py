"""

https://projecteuler.net/problem=5

"""

if __name__ == '__main__':

    check_divisible_by = list(range(11, 21))

    candidate = 2520

    while not all([candidate % i == 0 for i in check_divisible_by]):
        candidate += 20

    print(candidate)

