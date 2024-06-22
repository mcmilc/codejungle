def car_fueling_2(M, s, distance):
    pos = 0
    j = 0  # idx stops
    n_stops = 0
    max_pos = pos + M
    prev_j = 0
    while max_pos < distance:
        print("")
        print(f"max_pos: {max_pos}")
        while j < (len(s) - 1) and s[j] <= max_pos:
            j += 1
        j -= 1
        print(f"j is {j}")
        if j == prev_j:
            return -1
        try:
            pos += min(s[j], max_pos)
            print(f"pos is {pos}")
        except Exception as exc:
            print(f"j is {j}, n_stops is {n_stops}")
            return -1
        n_stops += 1
        max_pos = pos + M
        prev_j = j
        print("")
    return n_stops
