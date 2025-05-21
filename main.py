from stats import count_characters, count_words, sort_characters
from curses.ascii import isalpha

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents

def print_report(book, num_words, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for single_character in sorted_characters:

        if single_character["char"].isalpha():
            char = single_character["char"]
            count = single_character["num"]
            print(f"{char}: {count}")

    print("============= END ===============")

def main():
    frankenstein_book = "books/frankenstein.txt"

    content = get_book_text(frankenstein_book)

    num_words = count_words(content)
    # print(f"{num_words} words found in the document")

    num_characters = count_characters(content)
    # print(num_characters)

    sorted_characters = sort_characters(num_characters)

    print_report(frankenstein_book, num_words, sorted_characters)

if __name__ == "__main__":
    main()
