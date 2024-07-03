def arg_max(a):
    L = len(a)
    assert L > 0
    m = a[0]
    m_j = 0
    for i in range(L):
        if a[i] > m:
            m = a[i]
            m_j = i
    return m, m_j


def max_dot_product_it(p, c):
    L = len(p)
    assert L == len(c)
    assert L > 0
    if L == 1:
        return p[0] * c[0]
    j = 0
    dp = 0
    while j < L:
        _, m_p = arg_max(p)
        _, m_c = arg_max(c)
        dp += p.pop(m_p) * c.pop(m_c)
        j += 1
    return dp


def max_dot_product_rec(p, c):
    L = len(p)
    assert L == len(c)
    assert L > 0
    if L == 1:
        return p[0] * c[0]
    _, m_p = arg_max(p)
    _, m_c = arg_max(c)
    c_dp = p.pop(m_p) * c.pop(m_c)
    return c_dp + max_dot_product_rec(p, c)


if __name__ == "__main__":
    p = [23]
    c = [39]
    out = max_dot_product_it(p, c)
    pass
