def last_digit_fibonacci(n):
    y = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
    return y[n] % 10


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci(n))
