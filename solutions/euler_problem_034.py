"""
https://projecteuler.net/problem=34
"""

from itertools import combinations_with_replacement
from utils.factorial import factorial

from typing import Tuple


def sum_factorials(digits: Tuple[int]) -> int:
	return sum([factorial(digit) for digit in digits])


def digit_combination(n: int) -> Tuple[int]:
	d_comb = []
	while n:
		n, r = divmod(n, 10)
		d_comb.append(r)
	d_comb.reverse()
	return tuple(d_comb)


"""
Let us denote:
	n, a number
	S, the sum of the factorials of its digits
	k, the number of its digits

for any number n, the following statements are true:
	a)	0 < S <= k * 9!
	b)	10**(k-1) <= n < 10**k

Since we're interested in numbers where n=S, it must follow that:
	--> the minimum possible value of S must always be smaller than or equal to the greatest possible value of n.
	--> the maximum possible value of S must always be greater than or equal to the smallest possible value of n.

Therefore, for the set of all numbers where n == S, the following inequalities are true:
	c)	1 <= 10**k
	d)	k * 9! >= 10**(k-1)

From statement d, and knowing that k is an integer, we find:
	e) 	k <= 7
"""
K_MAX = 7


ZERO_FACTORIAL = factorial(0)


def solution():
	numbers = []

	"""
	The sum of factorials of digits of a number does not depend on the order of the digits:
		--> sum_factorials(637) = sum_factorials(736)
		--> 6! + 3! + 7! = 7! + 3! + 6!
	
	We can perform our search over the set of unique combinations of K_MAX digits
	"""
	for digit_comb in combinations_with_replacement(range(0, 10), K_MAX):
		if digit_comb == 7 * (0,):	# skipping the case where all digits are zero
			continue
		
		sum_fact_comb = sum_factorials(digit_comb)
		if 0 in digit_comb:
			# checking for every possible number of leading zeros in the combination of digits
			for n_leading_zeros in range(digit_comb.count(0) + 1):
				sum_fact = sum_fact_comb - n_leading_zeros * ZERO_FACTORIAL
				if sorted(digit_combination(sum_fact)) == sorted(digit_comb[n_leading_zeros:]):
					numbers.append(sum_fact)
		else:
			digits_sum_fact = digit_combination(sum_fact_comb)
			if sorted(digits_sum_fact) == sorted(digit_comb):
				numbers.append(sum_fact_comb)

	return sum(numbers) - 1 - 2		# "removing" the special cases of 1! and 2!


if __name__ == "__main__":
	print(solution())

