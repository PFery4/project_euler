"""

https://projecteuler.net/problem=22

instructions:
save the 'names.txt' file in the 'gitignored' folder.

"""

import os

def solution():

    filepath = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '../gitignored'))
    filename = 'p022_names.txt'

    with open(os.path.join(filepath, filename)) as file:
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
