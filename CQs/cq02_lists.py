"""Mutating functions."""

__author__ = "730739966"

def manual_append(a: list[int], b: int) -> None:
    a.append (b)
    return None

def double(a: list[int]) -> None:
    idx = 0
    while idx < len(a):
        a[idx] *= 2
        idx += 1
    return None

list_1: list[int] = [1,2,3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)