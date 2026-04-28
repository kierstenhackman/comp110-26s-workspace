"""Tea Party with Friends!"""

__author__ = "730739966"
# I had a lot of issues with this part because I thought I needed to replace author with my name! and then I was added a string function like the instructions said but it was getting flagged"


def main_planner(guests: int) -> None:
    """Print all values"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# I wanted to elimate the space between the $ and the cost, so I added them to remove the comma, but then got an error message that I had to convert the cost into a string value first


def tea_bags(people: int) -> int:
    """Number of tea bags needed"""
    return 2 * people


def treats(people: int) -> int:
    """Number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea party"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
