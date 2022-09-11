"""

https://projecteuler.net/problem=18

instructions:
copy-paste the pyramid into a file called 'problem_18_pyramid.txt' inside the 'gitignored' folder.

"""

import os

def solution():

    filepath = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '../gitignored'))
    filename = 'problem_18_pyramid.txt'

    with open(os.path.join(filepath, filename)) as file:
        lines = file.readlines()

    lines = [line.replace('\n', '').split(' ') for line in lines]
    lines = [[int(item) for item in line] for line in lines]

    for i in range(len(lines)-2, -1, -1):
        for j in range(len(lines[i])):
            lines[i][j] += max(lines[i+1][j], lines[i+1][j+1])
        lines.pop()

    return lines[0][0]


if __name__ == '__main__':
    print(solution())
