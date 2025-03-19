import sys



from stats import get_num_words
from stats import get_letter_count
from stats import sorted_letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
 
    num_word = get_num_words(book_text)
    num_letter = get_letter_count(book_text)
    alphabetically_sorted_letters = sorted_letter_count(num_letter)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"Found {num_word} total words")
    print("--------- Character Count -------")

    for letter in alphabetically_sorted_letters:
        if letter['character'].isalpha():
            print(f"{letter['character']}: {letter['count']}")
    print("============= END ===============")

main()