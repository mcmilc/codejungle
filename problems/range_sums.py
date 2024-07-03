"""
Based on problem 5.12 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner
"""


def range_sums(a, l, r):
    """
    Idea:

    For input array a:

    |---|                       s_r[0][0] = a_0
    |--------|                  s_r[1][0] = s_r[0][0] + a_1
    |------------------|        s_r[2][0] = s_r[1][0] + a_2
    |-----------------------|   s_r[3][0] = s_r[2][0] + a_3
    [a_0, a_1, a_2, a_3, a_4]

    Therefore:

    s_r[k][0] = s_r[k-1][0] + a_{k}

    Calculate sums for ranges that do not start at index 0 using:

                   |--------|   s_r[1][3] = s[4][0] - s[2][0]
    |-----------------------|   s_r[4][0]
    |-------------|             s_r[2][0]
    [a_0, a_1, a_2, a_3, a_4]

    Therefore for 0 <= l < n and l <= r < n - l:

    s_r[l][r] = s[l + r][0] - s[r - 1][0]
    """
    s_r = []
    n = len(a)
    assert l >= 0 and l < n
    assert r >= l and r < n - l
    s_r.append(a[0])
    for i in range(1, n):
        s_r.append(s_r[i - 1] + a[i])
    return s_r[l + r] - s_r[l]


def range_sums_indices(a, l, r):
    s_r = []
    n = len(a)
    assert l >= 0 and r >= 0
    assert r > l
    assert l + r <= n * 2 - 1
    s_r.append(a[0])
    for i in range(1, n):
        s_r.append(s_r[i - 1] + a[i])
    if l == 0 and r > 0:
        return s_r[r - 1]
    return s_r[r - 1] - s_r[l - 1]
