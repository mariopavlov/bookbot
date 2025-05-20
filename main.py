from stats import count_characters, count_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents


def main():
    frankenstein_book = "books/frankenstein.txt"

    content = get_book_text(frankenstein_book)

    num_words = count_words(content)
    print(f"{num_words} words found in the document")

    num_characters = count_characters(content)
    print(num_characters)


if __name__ == "__main__":
    main()
