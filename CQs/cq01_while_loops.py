"""While Loop Challenge Problem"""

__author__ = "730739966"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    return count


def get_evens(numbers: str) -> str:
    evens: str = ""
    index: int = 0
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            # i keep getting a note that says not all arguments converted during string formatting
            # i had changed it to int(numbers etc. but i was still getting the string error
            # exited and cleared my terminal and turns out i needed to re-import my function in order to run the updated version
            evens = evens + numbers[index]
        index += 1
    return evens
