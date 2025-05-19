
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        
        return file_contents

def main():
    frankenstein_book = "books/frankenstein.txt"

    content = get_book_text(frankenstein_book)

    print(content)

if __name__ == "__main__":
    main()

