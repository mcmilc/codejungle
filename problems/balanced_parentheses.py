from ..datastructures.stack import Stack


class PBCB:
    _charset_opening = "([{"
    _charset_closing = "}])"

    @classmethod
    def is_opening(cls, char):
        return char in cls._charset_opening

    @classmethod
    def is_closing(cls, char):
        return char in cls._charset_closing

    @classmethod
    def get_opposite_pbcb(cls, char):
        if char == "(":
            return ")"
        elif char == "{":
            return "}"
        elif char == "[":
            return "]"


class ParenthesisPair:
    def __init__(
        self, closed=False, opened=False, opening_char=None, closing_char=None
    ) -> None:
        self.closed = closed
        self.opened = opened
        self.opening_char = opening_char
        self.closing_char = closing_char

    def _is_valid(self):
        """
        Only used in __repr__
        """
        if self.opened and self.closed:
            return True

    def matches_opposite(self, char):
        return char == PBCB.get_opposite_pbcb(self.opening_char)

    def __repr__(self):
        if self._is_valid():
            return f"Valid node with content {self.opening_char}{self.closing_char}"
        else:
            return f"Invalid node with content {self.opening_char}{self.closing_char}"


def validate_parenthesis_pairs(s: str):
    invalid_nodes = []
    valid_nodes = []
    stack = Stack()
    for c in s:
        if PBCB.is_closing(c):
            if stack.is_empty():
                par_pair = ParenthesisPair(closed=True, closing_char=c)
                invalid_nodes.append(par_pair)
            else:
                par_pair = stack.pop()
                par_pair.closing_char = c
                if par_pair.matches_opposite(c):
                    par_pair.closed = True
                    valid_nodes.append(par_pair)
                else:
                    invalid_nodes.append(par_pair)
        elif PBCB.is_opening(c):
            par_pair = ParenthesisPair(opened=True, opening_char=c)
            stack.push(par_pair)
    return valid_nodes, invalid_nodes
