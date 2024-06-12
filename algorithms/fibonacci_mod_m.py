def fibonacci_mod_m(n, m):
    y = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
    return y[n] % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_mod_m(n, m))
