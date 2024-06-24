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


def max_loot(W, weights, costs):
    if W == 0:
        return 0
    assert len(weights) == len(costs)
    L = len(weights)
    costs_lbs = [costs[i] / weights[i] for i in range(L)]
    total_costs = 0
    while W > 0 and len(weights) > 0:
        _, max_j = arg_max(costs_lbs)
        amount = min(W, weights[max_j])
        weights[max_j] -= amount
        W -= amount
        total_costs += amount * costs_lbs[max_j]
        if weights[max_j] == 0:
            costs_lbs.pop(max_j)
            weights.pop(max_j)
    return round(total_costs, 3)


if __name__ == "__main__":
    W = 1000
    weights = [30]
    costs = [500]
    tot = max_loot(W, weights, costs)
    pass
