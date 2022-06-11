"""

https://projecteuler.net/problem=14

"""


def next_collatz(n):
    if n % 2 == 0:
        return n//2
    return 3 * n + 1


if __name__ == '__main__':

    starting_number = 13
    sequence = [starting_number]

    longest_starting_number = 0
    longest_sequence = []

    for i in range(1, 1_000_000):
        starting_number = i
        sequence = [starting_number]

        while sequence[-1] != 1:
            sequence.append(next_collatz(sequence[-1]))

        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
            longest_starting_number = i

    print(longest_starting_number)
