"""

https://projecteuler.net/problem=32

"""

import itertools

def process_tupl(num_tupl):
    """
    takes the num_tupl (a, b, c, d, e, f, g, h, i)
    returns the three ints: ab, cde, fghi
    """
    return int("".join(num_tupl[:2])), int("".join(num_tupl[2:5])), int("".join(num_tupl[5:]))

def solution():
    products = []
    for perm in itertools.permutations('123456789'):
        perm = "".join(perm)    # converting to a 9 digit string
        
        #checking for case: a * bcde = fghi
        n1, n2, n3 = int(perm[:1]), int(perm[1:5]), int(perm[5:])
        if n1 * n2 == n3:
            #print(f"{n1} * {n2} = {n3}")
            products.append(n3)
        
        #checking for case: ab * cde = fghi
        n1, n2, n3 = int(perm[:2]), int(perm[2:5]), int(perm[5:])
        if n1 * n2 == n3:
            #print(f"{n1} * {n2} = {n3}")
            products.append(n3)
    
    return sum(list(dict.fromkeys(products)))

if __name__ == "__main__":
	
	print(solution())

