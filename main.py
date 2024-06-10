def main():
    # path to the book
    book_path = "books/frankenstein.txt"
    # call the function to get text from the book
    text = get_book_text(book_path)
    # call the function to get number of words
    num_words = get_num_words(text)
    # call the function to get character dictionary
    chars_dict = get_chars_dict(text)
    # call the function to get sorted list of characters
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

# function that counts the number of words
def get_num_words(text):
    words = text.split()
    return len(words)

# function that sorts the dictionary
def sort_on(d):
    return d["num"]

# function that converts the dictionary to a sorted list
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# function that creates a dictionary of characters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

# function that reads the text from the book
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()