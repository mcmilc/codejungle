def fibonacci_sum(n):
    if n == 0:
        return 0, 0
    y = [0] * (n + 1)
    s = [0] * (n + 1)
    mods = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    s[0] = 0
    s[1] = 1
    mods[0] = 0
    mods[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        s[i] = s[i - 1] + y[i]
        mods[i] = s[i] % 10
    return y, s, mods


def last_digit_fibonacci_sum_fast(n):
    mods = [
        0,
        1,
        2,
        4,
        7,
        2,
        0,
        3,
        4,
        8,
        3,
        2,
        6,
        9,
        6,
        6,
        3,
        0,
        4,
        5,
        0,
        6,
        7,
        4,
        2,
        7,
        0,
        8,
        9,
        8,
        8,
        7,
        6,
        4,
        1,
        6,
        8,
        5,
        4,
        0,
        5,
        6,
        2,
        9,
        2,
        2,
        5,
        8,
        4,
        3,
        8,
        2,
        1,
        4,
        6,
        1,
        8,
        0,
        9,
        0,
    ]
    return mods[n % 60]


def last_digit_fibonacci_sum(n):
    if n == 0:
        return 0
    y_0 = 0
    y_1 = 1
    y_2 = 1
    s_1 = 1
    s_2 = 2
    i = 2
    while i < n:
        y_0 = y_1
        y_1 = y_2
        y_2 = y_1 + y_0
        s_1 = s_2
        s_2 = s_1 + y_2
        i += 1
    return s_2 % 10


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci_sum_fast(n))
