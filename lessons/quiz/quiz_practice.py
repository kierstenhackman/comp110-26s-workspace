
def odd_and_even(a: list[int]) -> list[int]:
    new: list[int] = []
    i: int = 0
    for i in range(0,len(a),2):
        if a[i] % 2 != 0:
            new.append(a[i])
    while i<len(a):
        if a[i] % 2 == 1 and i % 2 == 0:
            new.append(a[i])
        i+= 1
    
    return new


def short_words(a: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    result: list[str] = []
    for word in a:
        if len(word) < 5:
            result.append(word)
        else:
            print(f"{word} is too long")
    return result


def multiples(a: list[int]) -> list[bool]:
    result: list[bool] = []
    
    result.append(a[0] % a[len(a)-1] == 0)
    
    i: int = 1
    while i < len(a):
        result.append(a[i] % a[i-1] == 0)
        i += 1

    return result


def value_exists(a: dict[str,int], b: int) -> bool:
    for x in a:
        if a[x] == b:
            return True
    return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for x in inp:
        if inp[x] % 2 == 0:
            inp[x] += n
        else:
            inp[x] -= n



def free_biscuits(a: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for key in a:
        biscuits: list[int] = a[key]
        total: int = 0
        for elem in biscuits:
            total += elem 
        if total >= 100:
            result[key] = True
        else:
            result[key] = False
    return result