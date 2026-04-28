"""Exercise 4: List Utility Functions"""

__author__ = "730739966"

def all(a: list[int], b: int) -> bool:
    """Return True if all elements of a match b."""
    idx = 0
    if len(a) == 0:
        return False
    if len(a) < 1:
        return False
    while idx < len(a):
        if a[idx] != b:
            return False
        idx += 1
    return True

def max(input: list[int]) -> int:
    """Return the max number in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx = 1
    a = input[idx-1]
    while idx < len(input):
        if input[idx] > a:
            a = input[idx]
        idx += 1
    return a

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists"""
    idx = 0
    if len(list1) != len(list2): 
        return False
    while idx < len(list1): #because we've already made sure list1 and 2 are equal
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True

def extend(a: list[int], b: list[int]) -> None:
    """Extend list a with elements from list b."""
    idx = 0
    while idx < len(b): #need to individually add each element from b, not add list b as an individual element
        a.append(b[idx])
        idx += 1
    