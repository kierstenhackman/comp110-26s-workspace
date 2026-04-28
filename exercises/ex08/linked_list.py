"""Linked List Node and Utils Functions."""

__author__ = "730739966"


class Node:
    """A list Node storing my int value."""

    value: int
    next: "Node | None"

    def __init__(self, value: int, next: "Node | None"):
        """Initialize a node with a value and next node."""
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        """Return a string of the node chain."""
        return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return the max value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    rest_max = max(head.next)
    return head.value if head.value > rest_max else rest_max


def linkify(items: list[int]) -> Node | None:
    """Convert a list of ints to a linked list of Nodes with the same values in the same order."""
    if len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a new linked list of Nodes where each value of the original list is scaled by factor."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
