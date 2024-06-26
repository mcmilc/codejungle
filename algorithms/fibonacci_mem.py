def fibonacci(n):
    if n == 0:
        return 0
    y_0 = 0
    y_1 = 1
    y_2 = 1
    for _ in range(2, n):
        y_0, y_1 = y_1, y_2
        y_2 = y_1 + y_0
    return y_2


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
