"""
https://projecteuler.net/problem=22
"""

import os
from utils.data_directory import DATA_DIRECTORY
from utils.download_euler_file import download_file

FILE_NAME = '0022_names.txt'
download_file(FILE_NAME)


def solution():
    with open(os.path.join(DATA_DIRECTORY, FILE_NAME)) as file:
        names = file.readline()

    names = names.split(',')
    names = [item.replace("\"", "") for item in names]

    names = sorted(names)
    total = 0

    for position, name in enumerate(names):
        value = 0
        for letter in name:
            value += ord(letter) - ord('A') + 1
        score = (position + 1) * value
        total += score

    return total


if __name__ == '__main__':
    print(solution())
