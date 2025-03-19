def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_letter_count(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sorted_letter_count(letter_count):
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    # Transform the sorted tuples into dictionaries
    return [{'character': char, 'count': count} for char, count in sorted_letter_count]