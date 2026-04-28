"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730739966"


class River:
    """River with Bears and Fish."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Create new River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(num_fish):
            self.fish.append(Fish())
        for _ in range(num_bears):
            self.bears.append(Bear())

    def one_river_day(self):
        """Simulate one day of life in the River."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()

        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()

        print(self)

    def one_river_week(self):
        """Simulate one week of life in the River."""
        for _ in range(7):
            self.one_river_day()
        print(self)

    def __str__(self) -> str:
        """Update of Daily Population."""
        return f"~~~ Day {self.day}: ~~~\n Fish population: {len(self.fish)}\n Bear population: {len(self.bears)}"

    def check_ages(self):
        """Remove old Fish and Bears."""
        f = 0
        while f < len(self.fish):
            if self.fish[f].age > 3:
                self.fish.pop(f)
            else:
                f += 1
        b = 0
        while b < len(self.bears):
            if self.bears[b].age > 5:
                self.bears.pop(b)
            else:
                b += 1
        return None

    def remove_fish(self, amount: int):
        """Remove amount Fish from front of list."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Each Bear Eats 3 Fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove Starving Bears."""
        b = 0
        while b < len(self.bears):
            if self.bears[b].hunger_score < 0:
                self.bears.pop(b)
            else:
                b += 1
        return None

    def repopulate_fish(self):
        """Each Fish pair produces 4 offspring."""
        pairs = len(self.fish) // 2
        for _ in range(pairs * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Each Bear Pair produces 1 offspring."""
        pairs = len(self.bears) // 2
        for _ in range(pairs):
            self.bears.append(Bear())
        return None

    def __add__(self, r: River) -> River:
        """Add the quantities of two Rivers together."""
        total_fish: int = len(self.fish) + len(r.fish)
        total_bears: int = len(self.bears) + len(r.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> River:
        """Multiply the number of fish and bears in a River by factor."""
        return River((len(self.fish) * factor), (len(self.bears) * factor))
