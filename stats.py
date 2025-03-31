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


