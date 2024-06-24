"""
Finds 3rd largest value in array.
"""

import math


def third_largest_unique(a):
    """
    Find only truely unique values if a contains
    repetitions.
    """
    l = -math.inf
    sl = -math.inf
    tl = -math.inf
    n_comp = 0
    for i in a:
        n_comp += 1
        if i > l:
            tl = sl
            sl = l
            l = i
            continue
        elif i > sl:
            n_comp += 2
            # don't accept solution if it's equal to
            # largest
            if i != l:
                tl = sl
                sl = i
            continue
        elif i > tl:
            n_comp += 3
            # don't accept solution if it's equal to
            # largest or second largest
            if i != l and i != sl:
                tl = i
    return l, sl, tl, n_comp


def third_largest(a):
    l = -math.inf
    sl = -math.inf
    tl = -math.inf
    n_comp = 0
    for i in a:
        n_comp += 1
        if i > l:
            tl = sl
            sl = l
            l = i
            continue
        elif i > sl:
            n_comp += 1
            tl = sl
            sl = i
            continue
        elif i > tl:
            n_comp += 1
            tl = i
    return l, sl, tl, n_comp
