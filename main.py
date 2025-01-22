def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        list_of_words = file_contents.split()
        number_of_words = len(list_of_words)
        print(number_of_words)


main("books/frankenstein.txt")
