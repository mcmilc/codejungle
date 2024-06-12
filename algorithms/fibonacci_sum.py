def fibonacci_sum(n):
    if n == 0:
        return 0, 0
    y = [0] * (n + 1)
    s = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    s[0] = 0
    s[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        s[i] = s[i - 1] + y[i]
    return y, s


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))
