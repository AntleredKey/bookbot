from stats import get_num_words
from stats import get_count_characters
frankenstein = "./books/frankenstein.txt"

def get_book_text(book):
    booktext = ""
    with open(book) as f:
        booktext = f.read()
    return booktext

def main():
    booktext = get_book_text(frankenstein)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {frankenstein}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(booktext)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = get_count_characters(booktext)
    for character in character_count:
        if character[0].isalpha():
            print(f"{character[0]}: {character[1]}")
    print("============= END ===============")

main()
