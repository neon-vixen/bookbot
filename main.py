from stats import get_book_text
from stats import get_num_words
from stats import get_char_dict
from stats import get_sorted_dict
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_count = get_char_dict(book_text)
    sorted_char_list = get_sorted_dict(char_count)
    #print(f"{num_words} words found in the document")
    #print(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_char_list:
        print(f"{i["letter"]}: {i["count"]}")

main()