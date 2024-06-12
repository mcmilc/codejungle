def last_digit_partial_fibonacci_sum(m, n):
    assert m <= n
    if n == 0:
        return 0, 0
    y = [0] * (n + 1)
    s = [0] * ((n - m) + 1)
    y[0] = 0
    y[1] = 1
    if m == 0:
        s[0] = 0
        s[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        if i == m:
            s[i - m] = y[i]
        elif i > m:
            s[i - m] = s[i - m - 1] + y[i]
    return s[-1] % 10


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(last_digit_partial_fibonacci_sum(m, n))
