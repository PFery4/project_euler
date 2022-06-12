"""

https://projecteuler.net/problem=25

"""

if __name__ == '__main__':

    f_prev = 1
    f_curr = 1

    i_curr = 2
    while len(str(f_curr)) < 1000:
        f_next = f_prev + f_curr

        f_prev = f_curr
        f_curr = f_next
        i_curr += 1

    print(i_curr)
