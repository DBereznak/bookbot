import sys
from stats import get_num_words, sorted_chars
def get_book_text(path):
    with open(path) as file:
        return file.read()
    
def format_text(text, arg):
    word_count = get_num_words(text)
    char_char_count = sorted_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arg}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count -------")
    for item in char_char_count:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
    
def main():
    try:
        arg = sys.argv[1] if len(sys.argv) > 1 else None 
        if arg is None:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        text = get_book_text(arg)
        format_text(text, arg)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()