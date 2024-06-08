"""Queue data structure"""

from typing import Any
from . import base


class Queue(base.Storage):
    """Queue (FIFO)"""

    def pop(self) -> Any:
        """Return element using FIFO order. Element is removed from queue.

        Returns:
            Any: current element in FIFO queue
        """
        if self.size() > 0:
            # get and remove first element of array
            elem = self._elems[0]
            self._elems = self._elems[1:]
            return elem
