"""
Based on problem 6.3 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner

Example:
- 4 pounds saffron at 5000 $
- 3 pounds vanilla at 200 $
- 5 pounds cinnamon at 10 $

=> divide into value/pound

c_1 = 5000/w_1 => v_1 = 1250 $
c_2 = 200/3 => v_2 = 66.7 $
c_3 = 10/5 => v_3 = 2 $

Algo:

Input:
    total_compound_values: [v_1, v_2, v_3]
    total_compound_weights:  [w_1, w_2, w_3]
    backpack_weight: W
Output:
    Place compounds in backpack so its content is maximized.
    Return stolen value.

stolen_value <- 0
normalized_values <- [v_1/w_1, v_2/w_2, v_3/w_3]

# !super important!: check for whether we still have compunds left in while loop
while backpack is not full AND compounds left in inventory:
    max_i <- get index of max-value compound

    calc_weight <- calculate weight of max-value compound without exceeding backpack weight

    value_of_current_compound <- calculate the value

    put amount of compound into backpack

    update backpack weight

    subtract removed weight from inventory

    remove compound from inventory if its weight is zero

    update stolen value

return stolen_value
"""


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
