"""

https://projecteuler.net/problem=33

"""

def solution():

    numbers = []
    
    for tens in range(1,10):
        for units in range(1,10):
            number = int(f"{tens}{units}")
            numbers.append(number)
    
    
    nums = []
    denoms = []
    
    for idx, denom in enumerate(numbers):
        denom_tens = denom // 10
        denom_digits = denom % 10
        
        for num_tens in range(1, 10):
            if num_tens == denom_tens:
                continue
            
            if abs(int(f"{num_tens}{denom_tens}")/denom - num_tens/denom_digits) < 1e-10:
                # print(f"{num_tens}{denom_tens}/{denom} = {num_tens}/{denom_digits}")
                nums.append(num_tens)
                denoms.append(denom_digits)
    
    prod_num = 1
    prod_denom = 1
    for num, denom in zip(nums, denoms):
        prod_num *= num
        prod_denom *= denom
    
    # we could bother with making a general solution of reducing the fraction, but we know here that the final
    # irreducible version of the fraction is of the form 1/x, which means we can bypass this step.
    # the denominator is then equal to prod_denom / prod_num
    
    return prod_denom // prod_num

if __name__ == "__main__":
    print(solution())

