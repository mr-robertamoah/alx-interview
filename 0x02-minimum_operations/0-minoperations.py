#!/usr/bin/python3
"""
contains minOperations function
"""


def minOperations(n):
    """
    returns the minimun number of Copy All and Paste
    operations to perform to achieve n characters
    """
    if n < 2:
        return 0
    # start with no operations
    operations = 0
    # set factor to the lowest prime number
    factor = 2

    while n > 1:
        # ensure factor is a divisor of n
        while n % factor == 0:
            # set operations to the current factor
            # 1 Copy All operation and factor - 1 pastes
            operations += factor
            # reduce n to the remaining factor
            n //= factor
        # increase factor if it is not a divisor
        factor += 1

    return operations
