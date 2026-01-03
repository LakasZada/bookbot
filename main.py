import sys
from stats import get_num_words, count_char, char_report


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(filepath)
    char_counts = count_char(filepath)
    sorted_chars = char_report(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
main(filepath)
