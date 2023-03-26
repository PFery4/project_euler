"""

https://projecteuler.net/problem=42

"""

import os

def triang(n):
    return n * (n+1) // 2


def num_from(word):
    return sum([ord(l)-ord("A")+1 for l in word])


def is_triang(num):
    n = 1
    tri = triang(n)
    while tri <= num:
        if tri == num:
            return True
        n += 1
        tri = triang(n)
    return False


def solution():

    filepath = os.path.abspath(os.path.join(os.path.basename(os.path.dirname(__file__)), '../gitignored'))
    filename = 'p042_words.txt'

    with open(os.path.join(filepath, filename)) as file:
        words = file.readline()
    
    words = words.split(',')
    words = [item.replace("\"", "") for item in words]
    
    total = 0
    for word in words:
        total += is_triang(num_from(word))
        
    return total


if __name__ == '__main__':
    print(solution())

