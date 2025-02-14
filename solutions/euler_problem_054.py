"""
https://projecteuler.net/problem=54
"""

import os
from collections import Counter
from utils.data_directory import DATA_DIRECTORY
from utils.download_euler_file import download_file

from typing import List


FILE_NAME = '0054_poker.txt'
download_file(FILE_NAME)


# Hand Ranks
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9


class Card:

	VALUES = {str(n): int(n) for n in range(2, 10)} | dict(T=10, J=11, Q=12, K=13, A=14)
	SUITS = {str(c): str(c) for c in "CHSD"}

	def __init__(self, card_string: str):
		assert len(card_string) == 2
		self.card_string = card_string
		self.value = self.VALUES[self.card_string[0]]
		self.suit = self.SUITS[self.card_string[1]]

	def __repr__(self):
		return self.card_string


class Hand:

	def __init__(self, card_strings: List[str]):
		self.cards = [Card(card_string) for card_string in card_strings]

	def __repr__(self):
		return "-".join([card.__repr__() for card in self.cards])

	@property
	def values(self):
		return [card.value for card in self.cards]

	@property
	def sorted_values(self):
		return sorted(self.values)[::-1]	# from highest to lowest

	@property
	def suits(self):
		return [card.suit for card in self.cards]

	@property
	def is_flush(self) -> bool:
		return len(set(self.suits)) == 1

	@property
	def is_royal(self) -> bool:
		return self.sorted_values == list(range(14, 9, -1))

	@property
	def is_straight(self) -> bool:
		return all([v1 - v2 == 1 for v1, v2 in zip(self.sorted_values[:-1], self.sorted_values[1:])])

	@property
	def is_four_of_a_kind(self) -> bool:
		return self.get_value_counts() == [4, 1]

	@property
	def is_full_house(self) -> bool:
		return self.get_value_counts() == [3, 2]

	@property
	def is_three_of_a_kind(self) -> bool:
		return self.get_value_counts() == [3, 1, 1]

	@property
	def is_two_pairs(self) -> bool:
		return self.get_value_counts() == [2, 2, 1]

	@property
	def is_one_pair(self) -> bool:
		return self.get_value_counts() == [2, 1, 1, 1]

	@property
	def rank(self) -> int:
		if self.is_royal and self.is_flush:
			return ROYAL_FLUSH
		elif self.is_straight and self.is_flush:
			return STRAIGHT_FLUSH
		elif self.is_four_of_a_kind:
			return FOUR_OF_A_KIND
		elif self.is_full_house:
			return FULL_HOUSE
		elif self.is_flush:
			return FLUSH
		elif self.is_straight:
			return STRAIGHT
		elif self.is_three_of_a_kind:
			return THREE_OF_A_KIND
		elif self.is_two_pairs:
			return TWO_PAIRS
		elif self.is_one_pair:
			return ONE_PAIR
		else:
			return HIGH_CARD

	def __gt__(self, other):
		if self.rank == other.rank:
			compare_idx = 0
			while self.get_values_sorted_by_count()[compare_idx] == \
				other.get_values_sorted_by_count()[compare_idx]:
				compare_idx += 1
			return self.get_values_sorted_by_count()[compare_idx] > \
				other.get_values_sorted_by_count()[compare_idx]
		else:
			return self.rank > other.rank
	
	def get_sorted_value_counter(self) -> Counter:
		return Counter(self.sorted_values).most_common()

	def get_value_counts(self) -> List[int]:
		return [count for value, count in self.get_sorted_value_counter()]
	
	def get_values_sorted_by_count(self) -> List[int]:
		return [value for value, count in self.get_sorted_value_counter()]


def solution():
	with open(os.path.join(DATA_DIRECTORY, FILE_NAME)) as file:
		poker_hands = [line.rstrip().split(" ") for line in file]
		
	player_1_wins = 0
	for hands in poker_hands:
		hand_player_1, hand_player_2 = Hand(hands[:5]), Hand(hands[5:])
		player_1_wins += int(hand_player_1 > hand_player_2)

	return player_1_wins


if __name__ == '__main__':
	print(solution())

