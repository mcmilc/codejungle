from typing import List


class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children


class Graph:
    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = nodes
