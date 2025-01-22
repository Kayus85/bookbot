def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    number_of_words = count_words(file_contents)
    print(number_of_words)

def get_book_text(file):
    with open(file) as f:
        return f.read()

def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)


main("books/frankenstein.txt")
