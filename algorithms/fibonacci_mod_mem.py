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


def fibonacci_mod(n, m):
    y = [0] * (n + 1)
    mods = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        mods[i] = y[i] % m
    return y, mods


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_mod_mem(n, m))
