"""
Based on problem 6.7 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner

Input: Positive number
Output: Smallest number of integers that sum up to number

Approach:
- Use linked lists
- Use recursion by consistently adding 1 to recent sum-element
    - subtract current sum-element from target value
- If recent sum element exceeds target value -> stop
"""


class Node:
    def __init__(self, val, next_node: "Node"):
        self.val = val
        self.next = next_node

    def __str__(self):
        s = ""
        _node = self
        while _node.next is not None:
            s += f" {_node.val}"
            _node = _node.next
        # remember this last step => we stil have one value left
        # once we hit node.next = None
        s += f" {_node.val}"
        return s


def max_prices(node, input_value):
    print(f"Running start: {node.val} input_value: {input_value}")
    next_value = node.val + 1
    if input_value - next_value < next_value:
        node.next = Node(input_value, None)
        return
    else:
        node.next = Node(next_value, None)
        input_value -= next_value
        max_prices(node.next, input_value=input_value)


if __name__ == "__main__":
    node = Node(0, None)
    input_value = 45
    max_prices(node, input_value)
    print(str(node))
