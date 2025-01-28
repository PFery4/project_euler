"""
https://projecteuler.net/problem=42
"""

import os
from utils.data_directory import DATA_DIRECTORY
from utils.download_euler_file import download_file

FILE_NAME = '0042_words.txt'
download_file(FILE_NAME)


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
    with open(os.path.join(DATA_DIRECTORY, FILE_NAME)) as file:
        words = file.readline()
    
    words = words.split(',')
    words = [item.replace("\"", "") for item in words]
    
    total = 0
    for word in words:
        total += is_triang(num_from(word))
    return total


if __name__ == '__main__':
    print(solution())
