"""
Sieve of erastotheles algorithm for finding primes in range 0 - N.
import math
"""

import math


def get_primes_in_range(max_n):
    """Return list of prime numbers between 0 and N.

    Args:
        max_n (int): maximum number in range

    Returns:
        list: prime numbers
    """
    # include 0 and max_n itself as index
    idx_n = max_n + 1
    flags = [True] * idx_n

    # intialize flags array with flags[i] == True if i is prime
    flags[0] = flags[1] = False
    prime = 2

    # only iterate up to sqrt(max_n) but ensure using '<='
    while prime <= math.sqrt(max_n):
        # start with prime*prime because previous primes were already
        # checked off
        to_remove = prime * prime
        # creates slice of list starting at to_remove, stoping at idx_n
        # in steps of prime, example [4,6,8,10,...] (start with 2*2 in steps of 2)
        s_i = slice(to_remove, idx_n, prime)
        # flag multiples of current prime as False
        flags[s_i] = [False] * len(flags[s_i])
        # find next prime
        for i in range(to_remove + 1, idx_n):
            # locate next prime
            if not flags[i]:
                prime = i
                break
    return [j for j, c in enumerate(flags) if c]
