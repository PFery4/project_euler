"""

https://projecteuler.net/problem=11

Instructions:
Copy the grid, as it is presented in the problem, into a file in the 'gitignored' folder, called 'problem_11_grid.txt'

"""


def product(num_list):
    prod = 1
    for i in num_list:
        prod *= i
    return prod


def main():
    with open('../gitignored/problem_11_grid.txt') as file:
        grid = file.readlines()

    grid = [line.replace('\n', '').split(' ') for line in grid]
    grid = [[int(element) for element in line] for line in grid]

    n_rows = len(grid)
    n_cols = len(grid[0])

    greatest_product = 0

    for row_idx in range(n_rows):
        for col_idx in range(n_cols - 3):
            left_right = grid[row_idx][col_idx:col_idx+4]
            if 0 in left_right:
                continue
            if product(left_right) > greatest_product:
                greatest_product = product(left_right)

    for col_idx in range(n_cols):
        for row_idx in range(n_rows - 3):
            up_down = [grid[i][col_idx] for i in range(row_idx, row_idx+4)]
            if 0 in up_down:
                continue
            if product(up_down) > greatest_product:
                greatest_product = product(up_down)

    for row_idx in range(n_rows - 3):
        for col_idx in range(n_cols - 3):
            # '\' diagonal
            backward_diag = [grid[row_idx][col_idx+3],
                             grid[row_idx+1][col_idx+2],
                             grid[row_idx+2][col_idx+1],
                             grid[row_idx+3][col_idx]]
            if 0 in backward_diag:
                continue
            if product(backward_diag) > greatest_product:
                greatest_product = product(backward_diag)

            # '/' diagonal
            forward_diag = [grid[row_idx+3][col_idx],
                            grid[row_idx+2][col_idx+1],
                            grid[row_idx+1][col_idx+2],
                            grid[row_idx][col_idx+3]]
            if 0 in forward_diag:
                continue
            if product(forward_diag) > greatest_product:
                greatest_product = product(forward_diag)

    return greatest_product


if __name__ == '__main__':
    print(main())
