import sys
from stats import get_word_count, get_char_count, get_char_report

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def print_frankenstein():
    frankenstein = "books/frankenstein.txt"
    print(get_book_text(frankenstein))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookfile = sys.argv[1]
    contents = get_book_text(bookfile)
    words = get_word_count(contents)
    count = get_char_count(contents)
    report = get_char_report(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookfile}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for item in report:
        chr = item["char"]
        num = item["num"]
        if chr.isalpha():
            print(f"{chr}: {num}")

    print("============= END ===============")

main()
