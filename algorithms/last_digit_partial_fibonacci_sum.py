def last_digit_partial_fibonacci_sum(m, n):
    assert m <= n
    if n == 0:
        return 0
    y = [0] * (n + 1)
    s = [0] * ((n - m) + 1)
    mods = [0] * ((n - m) + 1)
    y[0] = 0
    y[1] = 1
    if m == 0:
        s[0] = 0
        s[1] = 1
        mods[0] = 0
        mods[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        if i == m:
            s[i - m] = y[i]
            mods[i - m] = s[i - m] % 10
        elif i > m:
            s[i - m] = s[i - m - 1] + y[i]
            mods[i - m] = s[i - m] % 10
    # return s[-1] % 10
    return y, s, mods


def last_digit_partial_fibonacci_sum_fast(m, n):
    _, _, mods = last_digit_partial_fibonacci_sum(m, 62)
    return mods[(n - m) % 60]


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(last_digit_partial_fibonacci_sum_fast(m, n))
