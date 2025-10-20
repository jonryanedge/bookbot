def sort_on(items):
    return items["num"]

def get_word_count(book):
    words = book.split()
    return len(words)

def get_char_count(book):
    char_tally = {}
    for char in book:
        char = char.lower()
        if char in char_tally:
            char_tally[char] += 1
        else:
            char_tally[char] = 1

    return char_tally

def get_char_report(count):
    tally = []
    for char, num in count.items():
        char_stats = {"char": char, "num": num}
        tally.append(char_stats)

    tally.sort(reverse=True, key=sort_on)
    return tally
