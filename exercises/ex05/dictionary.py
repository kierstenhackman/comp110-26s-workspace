"""Dictionary Exercise."""

__author__ = 730739966


def invert(input_values: dict[str, str]) -> dict[str, str]:
    """Invert input and output values."""
    output: dict[str, str] = {}
    
    for key in input_values:
        value = input_values[key]
        
        if value in output:
            raise KeyError("Duplicate key found!")
        
        output[value] = key
    return output


def favorite_color(colors: dict[str, str]) -> str:
    """Return most frequent color."""
    counting: dict[str, int] = {}   
    for name in colors:
#for every name in the colors function, fav is the value for each name. If fav was already counted in the empty dictionary, add 1 to amount. If it's the first time, value is 1. 
        fav = colors[name]
        if fav in counting:
            counting[fav] += 1
        else:
            counting[fav] = 1
    
    favorite = ""
    max = 0 
#could i put it in the same for in loop? kept separate for visual clearness for me personally 
    for name in colors:
        fav = colors[name]
        if counting[fav] > max:
#if the number of instances of favorite color in counting dictionary is greater than the max, then replace the value as the new max and the key as the new favorite.
            max = counting[fav]
            favorite = fav
    return favorite
     

def count(values: list[str]) -> dict[str, int]:
    """Count the number of times a value appears in a list."""
    result: dict[str, int] = {}
#storing values and the number of times it appears in the list
    for elem in values:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Sort a list of words into alphabetical categories."""
    result: dict[str, list[str]] = {}

    for word in list1:
        if len(word) > 0 and word[0].isalpha():
            first_letter: str = word[0].lower()
            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, name: str) -> None:
    """Update the attendance log."""
    if day in attendance:
        attendance[day].append(name)
    else:
        attendance[day] = [name]

    