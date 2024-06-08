"""Base class for Queue and Stack"""

from abc import abstractmethod
from typing import Any


class Storage:
    """Base class for Queue and Stack"""

    def __init__(self) -> None:
        self._elems = []

    def push(self, elem: Any) -> None:
        """Add new element

        Args:
            elem (Any): element to be added
        """
        self._elems.append(elem)

    def size(self) -> int:
        """Returns current number of elemens

        Returns:
            int: current number of elements
        """
        return len(self._elems)

    def is_empty(self):
        """Check if storage structure is empty.

        Returns:
            bool: True if structure is empty otherwise False
        """
        if not self._elems:
            return True
        return False

    @abstractmethod
    def pop(self) -> Any:
        raise NotImplementedError
