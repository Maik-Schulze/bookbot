def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        text = f.read()
    print(f"{get_num_words(text)} words found in the document.")

def get_num_words(text):
    return len(text.split())

main()