def is_not_vowel(character):
    if character.lower() not in "aeouei":
        return True
    return False


print("".join([char for char in input() if is_not_vowel(char)]))