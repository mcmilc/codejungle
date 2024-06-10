from datastructures.stack import Stack


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

    def is_valid(self):
        if self.opened and self.closed:
            return True

    def matches_opposite(self, char):
        return char == PBCB.get_opposite_pbcb(self.opening_char)

    def __repr__(self):
        if self.is_valid():
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
                node = ParenthesisPair(closed=True, closing_char=c)
                invalid_nodes.append(node)
            else:
                node = stack.pop()
                node.closing_char = c
                if node.matches_opposite(c):
                    node.closed = True
                    valid_nodes.append(node)
                else:
                    invalid_nodes.append(node)
        elif PBCB.is_opening(c):
            node = ParenthesisPair(opened=True, opening_char=c)
            stack.push(node)
    return valid_nodes, invalid_nodes
