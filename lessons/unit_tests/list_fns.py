


def get_first(xs: list[str]) -> str:
    return xs[0]

def remove_first(xs: list[str]) -> None:
    xs.pop(0)

def get_and_remove_first(xs: list[str]) -> list[str]:
    a = xs[0]
    xs.pop(0)
    return a