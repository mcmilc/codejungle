def min_fuel_stops(total_dist, dist_at_full, stops):
    stops.append(total_dist)
    L = len(stops)
    j = 0
    max_dist = dist_at_full
    c_p = 0
    n_stops = 0
    while j < L:
        to_drive = stops[j] - c_p
        if to_drive <= max_dist:
            max_dist -= to_drive
        else:
            if to_drive > dist_at_full:
                # we'll not make it even with full tank
                return -1
            else:
                max_dist = dist_at_full
                n_stops += 1
                continue
        c_p = stops[j]
        j += 1
    return n_stops


if __name__ == "__main__":
    # total_dist = 950
    # dist_at_full = 400
    # stops = [250, 375, 550, 750]
    total_dist = 10
    dist_at_full = 3
    stops = [1, 2, 5, 9]
    out = min_fuel_stops(total_dist, dist_at_full, stops)
    pass
