"""
https://projecteuler.net/problem=14
"""

from dataclasses import dataclass


@dataclass
class CollatzLink:
	value: int
	chain_len: int = None


COLLATZDICT = {1: CollatzLink(1, 1)}


def next_collatz(n: int) -> int:
	if n % 2 == 0:
		return n // 2
	return 3 * n + 1


def solution():
	longest_starting_number = 1
	longest_chain = 1
	for n in range(2, 1_000_000):
		checked_nums = [n]
		while checked_nums[-1] not in COLLATZDICT.keys():
			checked_nums.append(next_collatz(checked_nums[-1]))
		COLLATZDICT.update(
			{link: CollatzLink(link, COLLATZDICT[checked_nums[-1]].chain_len + dist_from_last) \
			for dist_from_last, link in enumerate(checked_nums[-2::-1], start=1)}
		)

		chain_len_candidate = COLLATZDICT[checked_nums[-1]].chain_len + len(checked_nums) - 1
		if chain_len_candidate > longest_chain:
			longest_starting_number = n
			longest_chain = chain_len_candidate

	return longest_starting_number


if __name__ == '__main__':
	print(solution())

