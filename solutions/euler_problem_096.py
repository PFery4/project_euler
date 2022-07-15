"""

https://projecteuler.net/problem=96

instructions:
download and save the file of the problem in the 'gitignored' folder, as 'p096_sudoku.txt'

"""


def make_sudoku_grid(line_block):
    """
    processes a block of lines from the file, into a list of lists of integers, making up the sudoku grid
    """
    line_block = line_block[1:]
    line_block = [line.replace("\n", "") for line in line_block]
    line_block = [[int(elem) for elem in line] for line in line_block]
    return line_block


def possible(grid, y, x, n):
    """
    determines whether a number can be placed in the sudoku grid, at location (x, y)
    :param grid: the sudoku grid, a list of lists of integers
    :param y: the y location (vertical)
    :param x: the x location (horizontal)
    :param n: the number itself
    :return: bool
    """
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve_sudoku(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, y, x, n):
                        grid[y][x] = n
                        solve_sudoku(grid)
                        grid[y][x] = 0
                break
    return grid


def print_sudoku_grid(grid):
    for index, line in enumerate(grid):
        str_line = ''.join([str(elem) for elem in line])
        str_line = str_line[:6] + "\U00002502" + str_line[6:]
        str_line = str_line[:3] + "\U00002502" + str_line[3:]
        str_line = " ".join(char for char in str_line)
        if index % 3 == 0 and index != 0:
            print(6 * "\U00002500" + "\U0000253C" + 7 * "\U00002500" + "\U0000253C" + 6 * "\U00002500")
        print(str_line)


def main():
    with open('../gitignored/p096_sudoku.txt') as file:
        lines = file.readlines()

    # for i in range(len(lines)//10):
    #     grid = make_sudoku_grid(lines[10*i:10*(i+1)])

    grid = make_sudoku_grid(lines[:10])

    print_sudoku_grid(grid)
    return


if __name__ == '__main__':
    print(main())
