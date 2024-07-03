"""Stack data structure"""

from typing import Any
from . import base


class Stack(base.Storage):
    """Stack (LIFO)"""

    def pop(self) -> Any:
        """Return element using LIFO order. Element is removed from stack.

        Returns:
            Any: current element in LIFO stack
        """
        if self.size() > 0:
            # get and remove last element of array
            elem = self._elements[-1]
            self._elements = self._elements[:-1]
            return elem
