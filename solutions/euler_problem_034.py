"""
https://projecteuler.net/problem=34
"""

from utils.factorial import factorial


def sum_factorials(n: int) -> int:
	return sum([factorial(int(i)) for i in str(n)])


def solution():
	total = 0
	for x in range(10, 10_000_000):
		if x == sum_factorials(x):
			total += x
	return total


if __name__ == "__main__":
	print(solution())
