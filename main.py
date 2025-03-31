import sys
from stats import get_book_text, count_words, count_char, sort_and_filter 

def main(path_to_file):

    
    file_contents = get_book_text(path_to_file)
    number_of_words = count_words(file_contents)
    char_stats = count_char(file_contents)
    filtered_characters = sort_and_filter(char_stats)

    # print report
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{number_of_words} words found in document")
    print("\n")
    for e in filtered_characters:
        print(f"The '{e["char"]}' character was found {e["count"]} times")
    print("--- End report ---")

if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main(sys.argv[1])
