#!/usr/bin/python3
"""
Prime game module with a isWinner function
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime number game played over several x.

    Parameters:
    - x (int): Number of x in the game.
    - nums (list): List of integers where each integer specifies the upper limit
                           for prime number counting in that round.

    Returns:
    - str: 'Maria' if Maria wins more rounds, 'Ben' if Ben wins more rounds, or None if tied.
    """
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    max_limit = max(nums)
    is_prime_list = [True] * (max_limit + 1)
    is_prime_list[0] = is_prime_list[1] = False

    for i in range(2, int(max_limit ** 0.5) + 1):
        if is_prime_list[i]:
            for j in range(i * i, max_limit + 1, i):
                is_prime_list[j] = False

    prime_counts = [0] * (max_limit + 1)
    prime_count = 0
    for i in range(1, max_limit + 1):
        if is_prime_list[i]:
            prime_count += 1
        prime_counts[i] = prime_count

    for limit in nums[:x]:
        if prime_counts[limit] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
