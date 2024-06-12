def fibonacci_sum(n):
    if n == 0:
        return 0
    y_0 = 0
    y_1 = 1
    y_2 = 1
    s_1 = 1
    s_2 = 2
    for i in range(2, n):
        y_0 = y_1
        y_1 = y_2
        y_2 = y_1 + y_0
        s_1 = s_2
        s_2 = s_1 + y_2
    return s_2


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))
