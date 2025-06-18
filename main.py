from stats import character_count, accept_text, sort_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    words = book_text.split()
    print(f"Found {len(words)} total words")
    
    letter_counts = character_count(book_text)
    sorted_counts = sort_list(letter_counts)
    print(letter_counts)

    for letter, count in sorted_counts:
        print(f"{letter}: {count}")

main()
