from stats import count_characters, count_words, sort_characters
import sys

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

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    book_to_analyse = sys.argv[1]
    # frankenstein_book = "books/frankenstein.txt"

    content = get_book_text(book_to_analyse)

    num_words = count_words(content)
    # print(f"{num_words} words found in the document")

    num_characters = count_characters(content)
    # print(num_characters)

    sorted_characters = sort_characters(num_characters)

    print_report(book_to_analyse, num_words, sorted_characters)

if __name__ == "__main__":
    main()
