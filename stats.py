def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letters = {}
    for i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def sort_on(items):
    return items["num"]

def count_list(dictionary):
    sorted_list = []
    for i in dictionary:
        counted_words = dictionary[i]
        new_dictionary = {"char": i, "num": counted_words}
        sorted_list.append(new_dictionary)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list