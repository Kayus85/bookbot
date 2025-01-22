def main(path_to_file):
    file_contents = get_book_text(path_to_file)
    number_of_words = count_words(file_contents)
    char_stats = count_char(file_contents)
    print(char_stats)
    # print(number_of_words)

def get_book_text(file):
    with open(file) as f:
        return f.read()

def count_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def count_char(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main("books/frankenstein.txt")
