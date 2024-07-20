"""
Based on problem 6.11 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner

Approach:
    - Depth-first -> look for leaf
    - mark all leaves as "invited" and their parents as "remove"
    - if a parent has at least one child that is invited -> remove parent
"""


class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children
        self.status = ""

    def __eq__(self, status):
        return self.status == status

    def __str__(self):
        s = ""
        s += f"Name: {self.name}\n"
        s += f"Status: {self.status}\n"
        s += "\n"
        if self.children is not None:
            for child in self.children:
                s += str(child)
        return s

    def is_invited(self):
        return self.status == "invited"


def explore(node: Node, parent: Node):
    if node.children is None:
        # we have reached a leaf
        node.status = "invited"
    else:
        tmp_status = "remove"
        for child in node.children:
            # recursive depth-first propagation to leaves
            explore(child, node)
            if child.status == "invited":
                # check if at least one child is invited
                tmp_status = "invited"
        if tmp_status == "invited":
            # if at least one child is invited remove parent
            node.status = "remove"
        else:
            # otherwise keep parent
            node.status = "invited"


def test_1():
    A = Node("A", None)
    explore(A, None)
    return str(A)


def test_2():
    B = Node("B", None)
    C = Node("C", None)
    D = Node("D", None)
    A = Node("A", [B, C, D])
    explore(A, None)
    return str(A)


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

    assert A == "invited"
    assert B == "invited"
    assert C == "invited"
    assert G == "invited"
    assert F == "invited"
    assert E == "invited"

    assert J == "remove"
    assert H == "remove"
    assert J == "remove"

    assert K == "invited"
