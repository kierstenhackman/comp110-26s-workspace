from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first

"""Testing Desired Outputs"""
def test_get_first_output() -> None:
    xs = ["a", "b", "c"]
    assert get_first(xs) == "a"

def test_get_and_remove_first_output() -> None:
    xs = ["x", "y", "z"]
    assert get_and_remove_first(xs) == "x"

"""Testing Desired Behaviors""" #remove part doesn't have an output

def test_remove_first_behavior() -> None:
    xs = ["a", "b", "c"]
    remove_first(xs)
    assert xs == ["b", "c"]

def test_get_and_remove_first_behavior() -> None:
    xs = ["x", "y", "z"]
    get_and_remove_first(xs)
    assert xs == ["y", "z"]
