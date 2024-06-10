from typing import Dict
from datastructures.graph import Node
from datastructures.queue import Queue


def breadth_first_search(root: Node, layer: Dict[Node, int], visited: Dict[Node, bool]):
    """Breadth-first search algorithm utilizing a Queue.

    Args:
        root (Node): node of a graph
        layer (Dict[Node, int]): layer[node] stores root <-> node disance
        visited (Dict[Node, bool]): visited[node] is True if node was explored
        before.
    """
    if root not in layer:
        layer = {root: 0}
    queue = Queue()
    visited.setdefault(root, True)
    queue.push(root)
    while queue.size() > 0:
        node = queue.pop()
        for child in node.children:
            if child not in visited:
                visited.setdefault(child, True)
                queue.push(child)
                layer.setdefault(child, layer[node] + 1)
