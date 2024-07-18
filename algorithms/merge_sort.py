import math


def merge_sort(a):
    A = len(a)
    if A == 2:
        if a[0] > a[1]:
            return [a[1], a[0]]
        else:
            return a
    if A == 1:
        return a
    Lh = math.floor(A / 2)
    left = a[:Lh]
    right = a[Lh:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(l, r):
    # l and r are sorted in ascending order
    L = len(l)
    R = len(r)
    C = L + R
    c = [None] * C
    i = 0
    j = 0
    k = 0
    while i < C:
        if j < L and k < R:
            if l[j] < r[k]:
                c[i] = l[j]
                i += 1
                j += 1
            else:
                c[i] = r[k]
                k += 1
                i += 1
        else:
            if j == L and k < R:
                c[i] = r[k]
                k += 1
                i += 1
            elif j < L and k == R:
                c[i] = l[j]
                j += 1
                i += 1
    return c


if __name__ == "__main__":
    a = [5, 4, 1, 8, 7, 2, 6, 3]
    out = merge_sort(a)
    pass
