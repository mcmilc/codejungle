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
    print(last_digit_fibonacci_sum(n))
