"""

https://projecteuler.net/problem=18

instructions:
copy-paste the pyramid into a file called 'problem_18_pyramid.txt' inside the 'gitignored' folder.

"""


if __name__ == '__main__':

    with open('../gitignored/problem_18_pyramid.txt') as file:
        lines = file.readlines()

    lines = [line.replace('\n', '').split(' ') for line in lines]
    lines = [[int(item) for item in line] for line in lines]

    for i in range(len(lines)-2, -1, -1):
        for j in range(len(lines[i])):
            lines[i][j] += max(lines[i+1][j], lines[i+1][j+1])
        lines.pop()

    print(lines[0][0])
