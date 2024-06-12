def fibonacci(n):
    if n == 0:
        return 0
    y = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
    return y[n]


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
