"""
Based on problem 6.2 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner
"""

import math

denominations = [10, 5, 1]


def get_max_denomination(money):
    # use the ordering of the list
    for d in denominations:
        if money >= d:
            return d


def money_change_greedy(money):
    """
    Greedy version.

    Compute the minimum number of coins needed to change the
    given value into coins with denominations 1, 5, and 10.

    Always select the coin with largest value for current value of money.
    """
    counter = 0
    while money > 0:
        d = get_max_denomination(money)
        money -= d
        counter += 1
    return counter


def money_change_one_liner(money):
    """
    math.floor(money / 10)       -> how many 10s coins do we need
                                    Example: 138 returns 13

    math.floor((money % 10) / 5) -> money % 10 returns last digit and / 5 tells
                                    us whether we need 1 or 0 5s coins
                                    Example: 138 returns 8 / 5 -> 1.6 -> 1

    math.floor(money % 5)        -> remainder of / 5 gives us number of 1s coins
                                    Example: 138 returns 3
    """
    return math.floor(money / 10) + math.floor((money % 10) / 5) + money % 5


if __name__ == "__main__":
    i = int(input())
    print(money_change_greedy(i))
