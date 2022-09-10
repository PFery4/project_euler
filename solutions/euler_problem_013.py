"""

https://projecteuler.net/problem=13

instructions:
copy-paste the numbers into a file called 'problem_13_lines.txt' inside the 'gitignored' folder

"""


def solution():
    with open('../gitignored/problem_13_lines.txt') as file:
        lines = file.readlines()

    lines = [int(line.replace("\n", "")) for line in lines]

    return str(sum(lines))[:10]


if __name__ == '__main__':
    print(solution())
