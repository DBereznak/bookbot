def get_num_words(text):
    words = text.split()
    return len(words)

def count_each_char(text):
    char_count = {}
    text = text.lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_chars(text):
    sorted_char_list = []
    char_count = count_each_char(text)
    for char in char_count:
        if char.isalpha():
            sorted_char_list.append({"char": char, "num": char_count[char]})
    sorted_char_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_char_list
