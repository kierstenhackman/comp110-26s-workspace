"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730739966"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    # initially forgot to put the def before input_word and was confusing myself for a while, went back and reviewed earlier lessons about function structure and set myself back on track
    word: str = input("Enter a 5-character word: ")

    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()

    return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    # initially forgot the spaces in here and got an all-in-one word
    count = 0

    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1

    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1

    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1

    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1

    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1

    if count > 0:
        if count == 1:
            print(str(count) + " instance of " + letter + " found in " + word)
            # forgot that 1 count would be instance instead of instances and needed a separate line of code
        else:
            print(str(count) + " instances of " + letter + " found in " + word)
        # forgot that count was not a str and was getting errors because i hadn't converted it in this line!
    else:  # was running into errors because my else was indented, then i had it on the same indent as if but there was accidentally a space before the else which was messing with the code
        print("No instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
