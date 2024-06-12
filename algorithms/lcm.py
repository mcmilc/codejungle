def gcd(n, m):
    """Greatest Common Divisor"""
    if n < m:
        tmp = m
        m = n
        n = tmp
    if n == 1 or m == 1:
        return 1
    if n == m:
        return n
    if m == 0:
        return n
    remainder = n % m
    if remainder == 0:
        return m
    else:
        return gcd(m, remainder)


def lcm(n, m):
    k = gcd(n, m)
    return int(n * m / k)


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(lcm(x, y))
