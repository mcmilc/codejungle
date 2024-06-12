def gcd(n, m):
    """Greatest Common Divisor"""
    if m == 0:
        return n
    else:
        if n > m:
            return gcd(m, n - m)
        else:
            return gcd(n, m - n)


def lcm(n, m):
    k = gcd(n, m)
    return n * m / k


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(lcm(x, y))
