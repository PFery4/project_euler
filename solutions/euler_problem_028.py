"""

https://projecteuler.net/problem=28

"""

if __name__ == '__main__':

    in_diag = [1]

    edge_length = 2
    n = 1

    while edge_length < 1001:
        for i in range(4):
            n += edge_length
            in_diag.append(n)
        edge_length += 2

    print(sum(in_diag))
