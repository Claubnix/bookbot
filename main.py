import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_dict_by_value

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ---------")
    num_words = get_num_words(get_book_text(book_path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(get_book_text(book_path))
    sorted_character_count = sort_dict_by_value(character_count)
    for character, count in sorted_character_count:
        print(f"{character}: {count}")
    print("============= END ===============")

# This is the entry point of the program
main()