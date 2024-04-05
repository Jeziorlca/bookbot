from collections import defaultdict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for k in count_letters_sorted(chars_dict):
        if k['key'].isalpha():
            print(f"The {k['key']} character was found {k['num']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    my_dict = defaultdict(int)
    for letter in text:
        my_dict[letter] += 1
    return my_dict

def sort_on(d):
    return d["num"]

def count_letters_sorted(mydict : dict):
    sorted = []
    for k in mydict:
        sorted.append({"key": k, "num": mydict[k]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted


main()