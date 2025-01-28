"""
https://projecteuler.net/problem=42
"""

import os
from urllib import request
from utils.data_directory import DATA_DIRECTORY

EULER_LINK = "https://projecteuler.net/resources/documents/0042_words.txt"
INPUT_FILE = os.path.join(DATA_DIRECTORY, "0042_words.txt")

if not os.path.exists(INPUT_FILE):
    request.urlretrieve(EULER_LINK, INPUT_FILE)
assert os.path.exists(INPUT_FILE)


def triang(n: int) -> int:
    return n * (n+1) // 2


def num_from(word: str) -> int:
    return sum([ord(char)-ord("A")+1 for char in word])


def is_triang(num: int) -> bool:
    n = 1
    tri = triang(n)
    while tri <= num:
        if tri == num:
            return True
        n += 1
        tri = triang(n)
    return False


def solution():
    with open(INPUT_FILE) as file:
        words = file.readline()
    
    words = words.split(',')
    words = [item.replace("\"", "") for item in words]
    
    total = 0
    for word in words:
        total += is_triang(num_from(word))
    return total


if __name__ == '__main__':
    print(solution())
