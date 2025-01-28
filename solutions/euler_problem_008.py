"""
https://projecteuler.net/problem=8

Instructions:
- Save the problem's number to 'data/problem_8.txt'.
"""

import os

INPUT_FILE = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '..', 'data', 'problem_8.txt'))
N_DIGITS = 13       # number of adjacent digits to be multiplied


def solution():

    with open(INPUT_FILE) as file:
        number = file.read().replace('\n', '')

    greatest_product = 0

    for index in range(len(number) - N_DIGITS + 1):

        if "0" in number[index:index+N_DIGITS]:
            continue

        product = 1
        for i in range(N_DIGITS):
            product *= int(number[index + i])
        if product > greatest_product:
            greatest_product = product

    return greatest_product


if __name__ == '__main__':
    print(solution())
