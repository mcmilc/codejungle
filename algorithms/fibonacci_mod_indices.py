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


def generate_fibonacci_modulos(n):
    """Generate one non-repetitve sequence of modulos for modulo n.

    Args:
        n (int): the modulo value
        L: for calculating
    """
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]
