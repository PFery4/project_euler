"""

https://projecteuler.net/problem=34

"""

from euler_problem_015 import factorial


def sum_factorials(n):
	return sum([factorial(int(i)) for i in str(n)])


def main():
	total = 0

	for x in range(10, 10000000):
		if x == sum_factorials(x):
			total += x

	return total


if __name__ == "__main__":
	print(main())
