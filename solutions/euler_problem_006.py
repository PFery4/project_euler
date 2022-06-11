"""

https://projecteuler.net/problem=6

"""

if __name__ == '__main__':

    sum_of_squares = 0

    for i in range(101):
        sum_of_squares += i * i

    print((50 * 101)**2 - sum_of_squares)
