"""
Based on problem 6.6 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner

Approach:
    1. Input comes in list of pairs [(l_1, p_1), (l_2, _p2), ..., (l_n, r_n)]
    2. Sort by l_i and init c_min_r as new r_1 or sorted segment array
    3. start while loop through all segments
    4. keep updating current c_min_r as long as incoming segments l_j are <= c_min_r
"""


def min_touch_segments_greedy(segments, intersections):
    if len(segments) == 0:
        return 0
    c_min_r = min(segments, key=lambda x: x[1])[1]
    to_remove = [s for s in segments if s[0] <= c_min_r]
    for r in to_remove:
        segments.remove(r)
    intersections.append(c_min_r)
    return 1 + min_touch_segments_greedy(segments, intersections)


def min_touch_segments(segments):
    L = len(segments)
    assert L > 0
    if L == 0:
        return 1
    segments = sorted(segments, key=lambda x: x[1])
    j = 1
    c_min_r = segments[0][1]
    counter = 1
    intersection_points = []
    while j < L:
        # is current segment's l_j <= c_min_r
        if segments[j][0] <= c_min_r:
            # is current segments r_j < c_min_r
            if segments[j][1] < c_min_r:
                # update c_min_r
                c_min_r = segments[j][1]
        else:
            intersection_points.append(c_min_r)
            counter += 1
            c_min_r = segments[j][1]
        j += 1
    # this is an important part since the
    # last line could be the one with the one
    # with the current minimum r point which means
    # that we never hit the "else" part
    intersection_points.append(c_min_r)
    return counter, intersection_points
