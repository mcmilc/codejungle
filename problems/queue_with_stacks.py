"""Implement a queue using two stacks"""

from ..datastructures.queue import Queue
from ..datastructures.stack import Stack


class PseudoQueue:
    """Queue class that is implemented via two stacks."""

    def __init__(self):
        self.stacks = [Stack(), Stack()]

        self.false_order_idx = 0
        self.correct_order_idx = 1

    def push(self, elem):
        """_summary_

        Args:
            elem (_type_): _description_
        """
        self.stacks[self.false_order_idx].push(elem)

    def pop(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.stacks[self.correct_order_idx].size() == 0:
            while self.stacks[self.false_order_idx].size() > 1:
                self.stacks[self.correct_order_idx].push(
                    self.stacks[self.false_order_idx].pop()
                )
            elem = self.stacks[self.false_order_idx].pop()
            return elem
        else:
            return self.stacks[self.correct_order_idx].pop()
