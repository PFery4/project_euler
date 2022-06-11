"""

https://projecteuler.net/problem=4

"""


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':

    number_1 = 999

    largest_palindrome = 0
    while number_1 >= 100:
        number_2 = 999
        while number_2 >= number_1:
            if number_1 * number_2 <= largest_palindrome:
                break
            if is_palindrome(number_1 * number_2):
                largest_palindrome = number_1 * number_2
            number_2 -= 1
        number_1 -= 1

    print(largest_palindrome)
