def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        text = f.read()
    char_dict = get_character_count(text)
    for char in char_dict:
        print(f"{char}: {char_dict[char]}")

def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    char_dict = {}
    text = text.lower()
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()