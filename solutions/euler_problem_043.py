"""
https://projecteuler.net/problem=43
"""

from itertools import permutations
from typing import List


def check_substring_div(nums: List[int]) -> bool:
    for k, prime in enumerate([2, 3, 5, 7, 11, 13, 17]):
        ddd = nums[k+1] * 100 + nums[k+2] * 10 + nums[k+3]
        if ddd % prime:
            return False  
    return True


def solution():
    total = 0
    for num_lst in permutations(str(1234567890)):
        nums = [int(num) for num in num_lst]
        num = sum([nums[i] * 10 ** (9 - i) for i in range(10)])
        if check_substring_div(nums):
            total += num
    return total


if __name__ == '__main__':
    print(solution())
