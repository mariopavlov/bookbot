def count_words(text):
    number_of_words = text.split()

    return len(number_of_words)

def count_characters(text):
    all_characters = {}

    for word in text.split():
        for char in word:
            char = char.lower()

            if char in all_characters:
                all_characters[char] = all_characters[char] + 1
            else:
                all_characters[char] = 1

    return all_characters
