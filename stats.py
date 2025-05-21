def count_words(text):
    number_of_words = text.split()

    return len(number_of_words)

def count_characters(text: str):
    all_characters = {}

    for word in text.split():
        for char in word:
            char = char.lower()

            if char in all_characters:
                all_characters[char] = all_characters[char] + 1
            else:
                all_characters[char] = 1

    return all_characters

def sort_characters(characters):
    """
    Combines characters and character counts into single dictionary.

    Parameters:
    characters (dictionary): All characters and their count

    Returns:
    dictionary: sorted dictionary of all characters. Sorted by count ocurence

    """
    character_list = []

    for char, count in characters.items():
        single_char = {
            "char": char,
            "num": count
        }

        character_list.append(single_char)

    sorted_characters = sorted(character_list, key=lambda x: x["num"], reverse=True)

    return sorted_characters
