def last_digit_fibonacci(n):
    if n == 0:
        return 0
    # y = [0] * (n + 1) -> will result in memory error for high n
    y_0 = 0
    y_1 = 1
    y_2 = 1
    for i in range(2, n):
        y_0 = y_1
        y_1 = y_2
        y_2 = y_1 + y_0
        # y[i] = y[i - 1] + y[i - 2]
    return y_2 % 10


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci(n))
