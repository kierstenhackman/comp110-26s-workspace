"""Wordle"""

__author__ = "730739966"


def input_guess(secret_length: int) -> str:
    """Is the guessed word the correct length?"""
    word: str = input(f"Enter a {secret_length} character word: ")
    while len(word) != secret_length:
        word = input(f"That wasn't {secret_length} chars! Try again: ")
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Is the guessed character in the secret word?"""
    assert len(char_guess) == 1
    i: int = 0

    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emoji string showing correctness of the guess."""

    assert len(guess) == len(secret)
    i: int = 0
    emoji_string: str = ""
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"

    while i < len(secret):
        if guess[i] == secret[i]:
            emoji_string += GREEN_BOX
            # originally was just printing GREEN_BOX instead of adding them all together into one string! needed to make a separate variable like we learned
        elif contains_char(secret, guess[i]):
            # originally was setting this condition equal to True and it wasn't working so i reviewed some class notes and realized that this section would only run if contains_char was true
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        i += 1
    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    current_turn: int = 1
    # originally had defined guess as one of my variables up here but that resulted in calling the input_guess function too early - i figured out that i could just define it later in the function and both define guess as a variable and call input_guess as a function in the same line of code

    while current_turn <= 6:
        print(f"=== Turn {current_turn}/6 ===")
        guess: str = input_guess(secret_length=len(secret))
        print(emojified(guess, secret))
        if secret == guess:
            print(f"You won in {current_turn}/6 turns!")
            return
        else:
            current_turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main(secret="codes")
