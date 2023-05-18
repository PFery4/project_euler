"""

https://projecteuler.net/problem=54

instructions:
save the 'p054_poker.txt' file in the 'gitignored' folder.

"""

import os


def hand_from(cardstring):
    """
    takes a string specifying the cards in a hand, and produces the value of the hand.
    """
    pass

def solution():

    filepath = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '../gitignored'))
    filename = 'p054_poker.txt'

    with open(os.path.join(filepath, filename)) as file:
        duels = file.readlines()
    
    for duel in duels:
        print(f"{duel[:14]} vs {duel[15:]}")

    return "WIP"


if __name__ == '__main__':
    print(solution())
