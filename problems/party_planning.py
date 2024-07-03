class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children
        self.status = None

    def __repr__(self):
        s = ""
        s += f"Name: {self.name}\n"
        s += f"Status: {self.status}\n"
        s += "\n"
        return s

    def is_invited(self):
        return self.status == "invited"


def explore(n: Node, parent: Node):
    if n.children is None:
        if parent is not None:
            parent.status = "remove"
        n.status = "invited"
    else:
        for child in n.children:
            explore(child, n)
        if any([child.is_invited() for child in n.children]):
            n.status = "remove"
        else:
            n.status = "invite"


def test_1():
    A = Node("A", None)
    explore(A, None)
    return A


def test_2():
    B = Node("B", None)
    C = Node("C", None)
    D = Node("D", None)
    A = Node("A", [B, C, D])
    explore(A, None)
    return A


def test_3():
    A = Node("A", None)
    B = Node("B", None)
    C = Node("C", None)
    G = Node("G", None)
    F = Node("F", None)
    D = Node("D", [A, B, C])
    E = Node("E", None)
    J = Node("J", [G])
    I = Node("I", [F])
    H = Node("H", [D, E])
    K = Node("K", [J, I, H])
    explore(K, None)
    return K
