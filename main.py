import sys
from stats import sort_on, dic_char, num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def fancy_print(chars, wordnum, text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}")
    print("----------- Word Count ----------")
    print(f"Found {wordnum} total words")
    print("--------- Character Count -------")
    sorted_chars = sorted(chars.items(), reverse=True, key=sort_on)
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    wordnum = num_words(get_book_text(book_path))
    chardic = dic_char(get_book_text(book_path))
    fancy_print(chardic, wordnum, book_path)

main()
