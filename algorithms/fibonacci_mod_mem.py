def fibonacci_last_digit(n):
    L = 60
    mods = [
        0,
        1,
        1,
        2,
        3,
        5,
        8,
        3,
        1,
        4,
        5,
        9,
        4,
        3,
        7,
        0,
        7,
        7,
        4,
        1,
        5,
        6,
        1,
        7,
        8,
        5,
        3,
        8,
        1,
        9,
        0,
        9,
        9,
        8,
        7,
        5,
        2,
        7,
        9,
        6,
        5,
        1,
        6,
        7,
        3,
        0,
        3,
        3,
        6,
        9,
        5,
        4,
        9,
        3,
        2,
        5,
        7,
        2,
        9,
        1,
    ]
    return mods[n % L]


def fibonacci_mod_mem(n, m):
    if n == 0:
        return 0
    y_0 = 0
    y_1 = 1
    y_2 = 1
    i = 2
    while i < n:
        y_0 = y_1
        y_1 = y_2
        y_2 = y_1 + y_0
        i += 1
    return y_2 % m


def fibonacci_mod_mem_fast(n, m):
    return n % (m + 1)


def fibonacci_mod(n, m):
    y = [0] * (n + 1)
    mods = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    mods[0] = 0
    mods[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        mods[i] = y[i] % m
    return y, mods


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_mod_mem_fast(n, m))
