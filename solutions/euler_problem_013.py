"""

https://projecteuler.net/problem=13

instructions:
copy-paste the numbers into a file called 'problem_13_lines.txt' inside the 'gitignored' folder

"""

import os

def solution():

    filepath = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '../gitignored'))
    filename = 'problem_13_lines.txt'

    with open(os.path.join(filepath, filename)) as file:
        lines = file.readlines()

    lines = [int(line.replace("\n", "")) for line in lines]

    return str(sum(lines))[:10]


if __name__ == '__main__':
    print(solution())
