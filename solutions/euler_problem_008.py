"""

https://projecteuler.net/problem=8

Instructions:
Copy the 1000 digit number, the same way it is presented, into a file in the 'gitignored' folder. This file should be named 'problem_8_number.txt'

"""

import os

def solution():

    filepath = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '../gitignored'))
    filename = 'problem_8_number.txt'

    with open(os.path.join(filepath, filename)) as file:
        lines = file.readlines()

    lines = [line.replace('\n', '') for line in lines]

    big_number_string = ''.join(lines)

    number_adjacent_digits = 13
    greatest_product = 0

    for index in range(len(big_number_string) - number_adjacent_digits + 1):

        if "0" in big_number_string[index:index+number_adjacent_digits]:
            continue

        number = 1
        for i in range(number_adjacent_digits):
            number *= int(big_number_string[index + i])
        if number > greatest_product:
            greatest_product = number

    return greatest_product


if __name__ == '__main__':
    print(solution())
