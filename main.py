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

def sort_and_filter(dict):
    list_from_dict = []
    for e in dict:
        list_from_dict.append({'char': e, 'count': dict[e]})

    list_from_dict.sort(key=sort_on_count, reverse=True)

    filtered = filter_alpha(list_from_dict)
    return filtered




def sort_on_count(dict):
    return dict["count"]

def filter_alpha(list):
    only_alpha = []
    for element in list:
        if element["char"].isalpha():
            only_alpha.append(element)
    return only_alpha

main("books/frankenstein.txt")
