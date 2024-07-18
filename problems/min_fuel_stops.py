"""
Based on problem 6.4 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner

Algo:
    Input:
        total_distance
        max_distance_at_full_tank
        number_of_stops

    Output:
        number_of_refills

    miles_driven = 0
    while miles_driven < total_distance:
        next_stop = max stop within max distance to drive # list comprehension
        if next_stop empty -> number_of_refills = -1 -> break
        else
        miles_driven += next_stop
        update max distance
        number_of_refills += 1

    return number_of_refills
"""

import math


def max(a):
    if len(a) == 0:
        return None
    m = -math.inf
    for item in a:
        if item > m:
            m = item
    return m


def min_fuel_stops_alternative(total_distance, stops, max_distance):
    distance_driven = 0
    number_of_refills = 0
    while max_distance < total_distance:
        next_stop = max(
            [stop for stop in stops if stop <= max_distance and stop > distance_driven]
        )
        if next_stop is None:
            return -1
        else:
            distance_driven = next_stop
            max_distance += distance_driven
            number_of_refills += 1
    return number_of_refills


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
    total_dist = 12
    dist_at_full = 3
    stops = [1, 2, 4, 5, 6, 7, 8, 10, 11, 12]
    out = min_fuel_stops(total_dist, dist_at_full, stops)
    out = min_fuel_stops_alternative(total_dist, stops, dist_at_full)
    pass
