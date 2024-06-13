from fibonacci_mod_mem import fibonacci_mod


def get_fibonacci_mod_indices(n, m):
    zero_indices = []
    idx = 0
    _, mods = fibonacci_mod(n, m)
    for i in mods:
        if mods[i] == 0:
            zero_indices.append(idx)
        idx += 1
    return zero_indices
