def last_digit_fibonacci_sum_of_sqaures(n):
    if n == 0:
        return 0, 0
    y = [0] * (n + 1)
    sq = [0] * (n + 1)
    y[0] = 0
    y[1] = 1
    sq[0] = 0
    sq[1] = 1
    for i in range(2, n + 1):
        y[i] = y[i - 1] + y[i - 2]
        sq[i] = y[i] * (y[i] + y[i - 1])
    return sq[n] % 10


if __name__ == "__main__":
    n = int(input())
    print(last_digit_fibonacci_sum_of_sqaures(n))
