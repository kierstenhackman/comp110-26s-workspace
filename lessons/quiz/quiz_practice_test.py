from lessons.quiz2.quiz2_function_writing import free_biscuits


def test_free_biscuits() -> None:
    xs = {"UNCvsDuke": [38, 20, 42], "UNCvsState": [9, 51, 16, 23]}
    assert free_biscuits(xs) == {"UNCvsDuke": True, "UNCvsState": False}