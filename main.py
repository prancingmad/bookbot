from stats import get_num_words
from stats import count_characters
from stats import count_list

import sys

test_line = 1

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    character_count = count_characters(book_text)
    most_list = count_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in most_list:
        character = i["char"]
        count = i["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")

main(sys.argv[1])