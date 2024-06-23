def josephus(n, k, debug=False):
    """O(n) time version of Josephus problem. Main idea is:

    [J(n, k) - k] % n = J[n-1, k]

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
