
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

        return file_contents

def count_words(text):
    number_of_words = text.split()

    return len(number_of_words)


def main():
    frankenstein_book = "books/frankenstein.txt"

    content = get_book_text(frankenstein_book)
    num_words = count_words(content)

    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
