def accept_text(book_text):
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document.")
    letter_counts = character_count(book_text)
    print(letter_counts)

def character_count(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_list(letter_counts):
    sorted_counts = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts