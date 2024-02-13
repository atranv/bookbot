def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} found in the document")
    char_count = get_char_count(text)
    sorted_char = sort_char(char_count)
    for char in sorted_char:
        print(char)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}

    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    return char_count

def sort_char(char_count):
    list_of_char = []
    for key, value in char_count.items():
        if key.isalpha():
            new_char_dic = {}
            new_char_dic["char"] = key
            new_char_dic["count"] = value
            list_of_char.append(new_char_dic)

    list_of_char.sort(reverse=True, key=lambda x: x["count"])
    return list_of_char

main()
