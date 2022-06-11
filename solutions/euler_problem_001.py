"""

https://projecteuler.net/problem=1

"""


if __name__ == '__main__':

    sum_multiples = 0

    candidate_number = 1
    while candidate_number < 1000:

        if candidate_number % 3 == 0 or candidate_number % 5 == 0:
            sum_multiples += candidate_number

        candidate_number += 1

    print(sum_multiples)


