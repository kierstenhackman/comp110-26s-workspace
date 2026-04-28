def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


pairs: list[dict[str, str]] = [
    {"owner": "Alyssa", "pet": "Bear"},
    {"owner": "Izzi", "pet": "Pip"},
    {"owner": "Kaki", "pet": "Lily"},
]
print(column_values(pairs, "pet"))


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


data_rows: list[dict[str, str]] = read_csv_rows("data_analysis/walter_wally.csv")
years: list[str] = column_values(data_rows, "year")


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def value_at(head: Node | None, index: int) -> int:
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    rest_max = max(head.next)
    return head.value if head.value > rest_max else rest_max


def linkify(items: list[int]) -> Node | None:
    if len(items) == 0:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
