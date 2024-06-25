def get_n_digits(n):
    assert n >= 0
    d = 10
    n_digits = 1
    if n == d:
        return 2
    while n > d:
        d *= 10
        n_digits += 1
        if n == d:
            return n_digits + 1
    return n_digits


def is_better(n1, n2):
    n_digits_1 = get_n_digits(n1)
    n_digits_2 = get_n_digits(n2)
    scale_1 = n1 * 10**n_digits_2 + n2
    scale_2 = n2 * 10**n_digits_1 + n1
    if scale_1 > scale_2:
        return n1
    else:
        return n2


def get_best(a):
    m = a[0]
    for i in a:
        b = is_better(m, i)
        m = b
    return m


def max_salary(a):
    out = []
    L = len(a)
    while L > 0:
        best = get_best(a)
        out.append(best)
        a.remove(best)
        L = len(a)
    return "".join(map(str, out))


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_salary(input_numbers))
