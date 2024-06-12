def gcd(n, m):
    """Greatest Common Divisor"""
    if n == 1 or m == 1:
        return 1
    if n > m:
        if m > n / 2:
            return 1
    elif m > n:
        if n > m / 2:
            return 1
    if n == m:
        return n
    if m == 0:
        return n
    else:
        if n > m:
            return gcd(m, n - m)
        else:
            return gcd(n, m - n)


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(gcd(x, y))
