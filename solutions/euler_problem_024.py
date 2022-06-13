"""

https://projecteuler.net/problem=24

"""

def str_permutations(string):
    if len(string) == 0:
        return []
    if len(string) == 1:
        return [string]

    l = []
    for i in range(len(string)):
        m = string[i]
        rem_str = string[:i] + string[i+1:]

        for p in str_permutations(rem_str):
            l.append(m + p)
    return l


if __name__ == '__main__':

    for i, p in enumerate(str_permutations('0123456789')):
        if i == 999_999:
            print(p)


