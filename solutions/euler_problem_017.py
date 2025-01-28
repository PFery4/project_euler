"""

https://projecteuler.net/problem=17

"""

from typing import List


NUM_2_WORD = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "one hundred",
    200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
    600: "six hundred", 700: "seven hundred", 800: "eight hundred",
    900: "nine hundred", 1000: "one thousand", 0: ""
}


def separate_number(n: int) -> List[int]:
    # separate the number into its decimal components
    splitnum = [int(digit) for digit in str(n)]
    ks = [10**i for i in range(len(str(n)))][::-1]
    array = [num * k for num, k in zip(splitnum, ks)]
    return array


def number_to_word(n: int) -> str:
    try:
        return NUM_2_WORD[n]
    except:
        if len(str(n)) == 2:
            return NUM_2_WORD[separate_number(n)[0]] + ' ' + NUM_2_WORD[separate_number(n)[1]]
        if len(str(n)) == 3:
            if separate_number(n)[1] // 10 == 1:
                return NUM_2_WORD[separate_number(n)[0]] + ' and ' + NUM_2_WORD[sum(separate_number(n)[1:])]
            else:
                return NUM_2_WORD[separate_number(n)[0]] + ' and ' + NUM_2_WORD[separate_number(n)[1]] + ' ' + \
                       NUM_2_WORD[separate_number(n)[2]]


def solution():
    total = 0
    for i in range(1, 1001):
        total += (len(number_to_word(i)) - number_to_word(i).count(' '))
    return total


if __name__ == '__main__':
    print(solution())
