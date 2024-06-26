def last_digit_partial_fibonacci_sum(m, n):
    if n == 0:
        return 0
    y = [0] * (n + 1)
    s = [0] * ((n - m) + 1)
    mods = [0] * ((n - m) + 1)
    y[0] = 0
    y[1] = 1
    if m >= 0:
        mods[0] = 0
        s[0] = 0
        if len(s) >= 2:
            s[1] = 1
            mods[1] = 1
        if len(s) >= 3:
            s[2] = 2
            mods[2] = 2
    elif m >= 1:
        s[0] = 1
        mods[0] = 1
        if len(s) >= 2:
            s[1] = 2
            mods[1] = 2
        if len(s) >= 3:
            s[2] = 4
            mods[2] = 4
    i = 2
    while i < n:
        y[i] = y[i - 1] + y[i - 2]
        if i == m:
            s[i - m] = y[i]
            mods[i - m] = s[i - m] % 10
        elif i > m:
            s[i - m] = s[i - m - 1] + y[i]
            mods[i - m] = s[i - m] % 10
        i += 1
    return y, s, mods


def last_digit_partial_fibonacci_sum_fast(m, n):
    assert 0 <= m <= n <= 1e14
    _, _, mods = last_digit_partial_fibonacci_sum(m, 62)
    idx = (n - m) % 60
    print(f"Idx: {idx}, len: {len(mods)}")
    assert idx < len(mods)
    return mods[idx]


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(last_digit_partial_fibonacci_sum_fast(m, n))
