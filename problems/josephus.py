def josephus_greedy(n, k, debug=False):
    i = 0
    n_s = n
    c = 0
    r = [True] * n
    idx = 0
    while n_s > 0:
        idx = i % n
        if r[idx]:
            if n_s == 1:
                break
            if c == k - 1:
                r[idx] = False
                n_s -= 1
                c = 0
            else:
                c += 1
        i += 1
    return idx


def josephus(n, k, debug=False):
    """O(n) time version of Josephus problem. Main idea is:

    [J(n, k) - k] % n = J[n-1, k]
    [J(n + 1, k) - k] % n = J[n, k]
    We are inverting this equation into:

    Assuming:
    J[n, k] = r

    Then:
    J[n + 1, k] = [r + k] % (n + 1)
    """
    # we start with n = 2 i.e. J(2, k) which always equals to k % 2
    c = 2
    j = k % 2
    while c < n:
        c += 1
        j = (j + k) % c
        if debug:
            print(f"J({c}, {k}): {j}")
    return j


if __name__ == "__main__":
    idx = josephus_greedy(13, 3)
    pass
