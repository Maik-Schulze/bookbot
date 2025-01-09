# BookBot

BookBot is a simple Python project that reads a text file, counts the number of words, and generates a character frequency report.

## Project Structure
.gitignore
books/frankenstein.txt
main.py
README.md

## How to Run

1. Make sure you have Python installed on your system.
2. Place the text file you want to analyze in the `books/` directory.
3. Update the `path` variable in `main.py` to point to your text file.
4. Run the script:

```sh
python main.py
```

## Output
The script will print a report to the console, showing the number of words in the document and the frequency of each character.

## Example
For the file `Frankenstein.txt`, the output might look like this:
```
--- Begin report of books/frankenstein.txt ---
77986 words found in the document

The 'e' character was found 46043 times
The 't' character was found 30365 times
...
--- End report ---
```
## License
This project is licensed under the MIT License.
Feel free to customize it further based on your needs!