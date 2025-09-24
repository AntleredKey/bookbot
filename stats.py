num_words = 0
characters = {}
characters_list = []

def get_num_words(booktext):
    num_words = len(booktext.split())
    return num_words

def sort_on(items):
    return items["num"]

def get_count_characters(booktext):
    lowertext = booktext.lower()
    for i in range(len(lowertext)):
        character = lowertext[i]
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    character_items = characters.items()
    characters_list = list(character_items)
    characters_list.sort(reverse=True, key=lambda x: x[1])
    return characters_list