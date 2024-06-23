"""
Based on problem 5.11 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner
"""

import numpy as np


def josephus_2(n):
    """Josephus problem for k=2.

    The first round around the circle eliminates all
    odd numbered positions. We therefore only need to
    care about the ceil(n/2) remaining even numbered
    positions.

    1) If n is even starting position is always 0
    2) If n is odd starting position is n - 1.

    """
    if n == 2:
        return 0
    elif n == 3:
        return 2
    elif n % 2 == 0:
        # n is even -> problem reduces to result for n/2 times 2.
        return josephus_2(int(n / 2)) * 2
    else:
        # n is odd -> prolem reduces to ceil(n/2) but indexing starts at n - 1
        n_h = int(np.ceil(n / 2))
        return (2 * josephus_2(n_h) - 2) % (n + 1)
