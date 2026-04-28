"""File to define Fish class."""


class Fish:
    """Fish Class."""

    age: int

    def __init__(self):
        """Define New Fish with age 0."""
        self.age = 0

    def one_day(self):
        """Age Fish by 1."""
        self.age += 1
