def last_digit_partial_fibonacci_sum(m, n):
    assert m <= n
    if n == 0:
        return 0
    y_0 = 0
    y_1 = 1
    y_2 = 1
    if m == 0:
        s_1 = 1
        s_2 = 2
    i = 2
    while i < n:
        y_0 = y_1
        y_1 = y_2
        y_2 = y_1 + y_0
        if i == (m - 1):
            s_2 = y_2
        elif i >= m:
            s_1 = s_2
            s_2 = s_1 + y_2
        i += 1
    return s_2 % 10


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(last_digit_partial_fibonacci_sum(m, n))
