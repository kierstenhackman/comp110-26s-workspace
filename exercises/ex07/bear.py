"""File to define Bear class."""


class Bear:
    """Bear Class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Define New Bears with age 0 and hunger_score 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Age Bear by 1 and decrease hunger_score by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase hunger_score by fish eaten."""
        self.hunger_score += num_fish
