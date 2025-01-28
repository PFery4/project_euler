"""
https://projecteuler.net/problem=22
"""

import os
from urllib import request
from utils.data_directory import DATA_DIRECTORY

EULER_LINK = "https://projecteuler.net/resources/documents/0022_names.txt"
INPUT_FILE = os.path.join(DATA_DIRECTORY, '0022_names.txt')

os.makedirs(DATA_DIRECTORY, exist_ok=True)
if not os.path.exists(INPUT_FILE):
    request.urlretrieve(EULER_LINK, INPUT_FILE)
assert os.path.exists(INPUT_FILE)


def solution():

    with open(INPUT_FILE) as file:
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
