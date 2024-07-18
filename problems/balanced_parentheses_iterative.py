def found_open(c):
    return c == "(" or c == "{" or c == "["


def found_closed(c):
    return c == ")" or c == "}" or c == "]"


def is_matching_pair(oc, cc):
    return (
        (oc == "(" and cc == ")")
        or (oc == "[" and cc == "]")
        or (oc == "{" and cc == "}")
    )


def match_parenthesis_pairs_iterative(s):
    state = "s"  # 's' = searching, 'fo' = "found open",  'fc' = "found closed"
    valid = []
    L = len(s)
    p_1 = 0
    p_2 = 0
    o_c = ""
    o_c_p = 0
    c_c = ""
    c_c_p = 0
    while p_1 < L and p_1 >= 0:
        if state == "s":
            # we didn't find an opening parenthesis yet
            if found_open(s[p_1]):
                # we have found an opening parenthesis
                # store character
                o_c = s[p_1]
                # store position
                o_c_p = p_1
                state = "fo"
            p_1 += 1
        elif state == "fo":
            # we're pointing to the most recent opening parenthesis
            if found_closed(s[p_1]):
                # we have found a closing parenthesis
                state = "fc"
                # store character and position
                c_c = s[p_1]
                c_c_p = p_1
                if is_matching_pair(o_c, s[p_1]):
                    # the closing parenthesis matches the opening one right away
                    # store characters and positions
                    valid.append((o_c, s[p_1], o_c_p, p_1))
                    # remove from character list
                    s[o_c_p : p_1 + 1] = []
                    # get new length of string
                    L = len(s)
                    # start from beginning
                    p_1 = 0
                    state = "s"
                    continue
                else:
                    # otherwise move backwards to find matching open parenthesis
                    p_1 -= 1
            else:
                o_c = s[p_1]
                o_c_p = p_1
                p_1 += 1
        elif state == "fc":
            # we have a closing parenthesis and we're looking for an
            # opening one backwards
            if found_open(s[p_1]):
                o_c = s[p_1]
                o_c_p = p_1
                if is_matching_pair(o_c, c_c):
                    valid.append((o_c, c_c, o_c_p, c_c_p))
                    s[o_c_p : c_c_p + 1] = []
                    L = len(s)
                    p_1 = 0
                    state = "s"
                    continue
                else:
                    p_1 -= 1
                if p_1 < 0:
                    # we didn't find an opening parenthesis for the current closing one
                    if c_c_p <= L - 3:
                        # if possible move past the curren closing parenthesis
                        p_1 = c_c_p + 1
                        state = "s"
    return valid


if __name__ == "__main__":
    s = "{{{{(}[]]]())"
    s = [c for c in s]
    valid = match_parenthesis_pairs_iterative(s)
