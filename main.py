def main():
    path = "books/frankenstein.txt"
    
    text = read_file(path)

    word_count = get_num_words(text)
    char_dict = get_character_count(text)

    for char in char_dict:
        print(char_dict)

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

main()