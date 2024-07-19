"""
Based on problem 5.12 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner
"""


def range_sums(a, left, right):
    """
    Idea:

    For input array a:

    |---|                       sum_range[0][0] = a_0
    |--------|                  sum_range[1][0] = sum_range[0][0] + a_1
    |------------------|        sum_range[2][0] = sum_range[1][0] + a_2
    |-----------------------|   sum_range[3][0] = sum_range[2][0] + a_3
    [a_0, a_1, a_2, a_3, a_4]

    Therefore:

    sum_range[k][0] = sum_range[k-1][0] + a_{k}

    Calculate sums for ranges that do not start at index 0 using:

                   |--------|   sum_range[1][3] = s[4][0] - s[2][0]
    |-----------------------|   sum_range[4][0]
    |-------------|             sum_range[2][0]
    [a_0, a_1, a_2, a_3, a_4]

    Therefore for 0 <= l < n and l <= r < n - l:

    sum_range[l][r] = s[l + r][0] - s[r - 1][0]
    """
    sum_range = []
    n = len(a)
    assert left >= 0 and left < n
    assert right >= left and right < n - left
    sum_range.append(a[0])
    for i in range(1, n):
        sum_range.append(sum_range[i - 1] + a[i])
    return sum_range[left + right] - sum_range[left]


def range_sums_indices(a, left, right):
    sum_range = []
    n = len(a)
    assert left >= 0 and right >= 0
    assert right > left
    assert left + right <= n * 2 - 1
    sum_range.append(a[0])
    for i in range(1, n):
        sum_range.append(sum_range[i - 1] + a[i])
    if left == 0 and right > 0:
        return sum_range[right - 1]
    return sum_range[right - 1] - sum_range[left - 1]
