"""

https://projecteuler.net/problem=8

"""

if __name__ == '__main__':

    with open('../gitignored/problem_8_number.txt') as file:
        lines = file.readlines()

    lines = [line.replace('\n', '') for line in lines]

    big_number_string = ''.join(lines)

    number_adjacent_digits = 13
    greatest_product = 0

    for index in range(len(big_number_string) - number_adjacent_digits + 1):

        if "0" in big_number_string[index:index+number_adjacent_digits]:
            continue

        number = 1
        for i in range(number_adjacent_digits):
            number *= int(big_number_string[index + i])
        if number > greatest_product:
            greatest_product = number

    print(greatest_product)
