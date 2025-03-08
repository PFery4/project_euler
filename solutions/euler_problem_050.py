"""
https://projecteuler.net/problem=50
"""


from utils.prime_numbers import primes_up_to


PRIMES = primes_up_to(1_000_000)


def solution():
    consec_p_sum = lambda idx_0, length: sum(PRIMES[idx_0: idx_0 + length])

    max_chain_len = 0
    while sum(PRIMES[:max_chain_len]) < PRIMES[-1]:
        max_chain_len += 1
    max_chain_len -= 1

    for longest_chain in range(max_chain_len, 0, -1):
        start_idx = 0
        answer = consec_p_sum(start_idx, longest_chain)
        while answer < PRIMES[-1]:

            if answer in PRIMES:
                return answer
            start_idx += 1
            answer = consec_p_sum(start_idx, longest_chain)


if __name__ == '__main__':
    print(solution())

