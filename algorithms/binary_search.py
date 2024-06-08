"""
look for number n within range [a, b] with a < b
or within sorted array ar with a = ar[0] and b = ar[-1]
while a <=b
    1. define mid-point mid = (a + b)/2
    2. if mid == n
        done!
    3. if n < mid
        b = mid
    4. else
        a = mid
    5. GoTo 1.
"""

import math
from typing import List
from typing import SupportsFloat


def binary_search(sorted_array: List[SupportsFloat], n: SupportsFloat) -> int:
    """Binary search algorithm

    Args:
        sorted_array (List[SupportsFloat]): Sorted array with numeric values
        n (SupportsFloat): The number we're looking for

    Returns:
        int: -1 if not found otherwise index of array that contains the n
    """
    if not sorted_array:
        return -1
    elif len(sorted_array) == 1:
        return 1
    a = 0
    b = len(sorted_array) - 1
    while a <= b:
        idx = math.ceil((a + b) / 2)
        if sorted_array[idx] == n:
            return idx
        elif sorted_array[idx] > n:
            b = idx - 1
        else:
            a = idx + 1
    return -1
