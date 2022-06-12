"""

https://projecteuler.net/problem=48

"""

if __name__ == '__main__':
    print(str(sum([i**i for i in range(1, 1001)]))[-10:])
