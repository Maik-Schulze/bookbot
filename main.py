def main():
    path = "books/frankenstein.txt"
    text = read_file(path)
    
    word_count = get_num_words(text)
    char_dict = get_character_count(text)
    characters = get_character_report(char_dict)

    print_character_report(characters, path, word_count)


def read_file(path):
    with open(path) as f:
        text = f.read()
    return text

def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(dict):
    return dict["count"]

def get_character_report(dict):
    characters = []
    for char in dict:
        if char.isalpha():
            characters.append({"char": char, "count": dict[char]})
    characters.sort(reverse=True, key=sort_on)
    return characters

def print_character_report(characters, path, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for c in characters:
        print(f"The \'{c["char"]}\' character was found {c["count"]} times")
    print("--- End report ---")

main()