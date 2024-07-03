def touch_segments(segments):
    L = len(segments)
    assert L > 0
    if L == 0:
        return 1
    segments = sorted(segments, key=lambda x: x[0])
    j = 1
    c_min_r = segments[0][1]
    segments.pop(0)
    counter = 0
    while j < L:
        if segments[j][0] <= c_min_r:
            if segments[j][1] < c_min_r:
                c_min_r = segments[j][1]
        else:
            counter += 1
            c_min_r = segments[j][1]
        j += 1
    return counter
