def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    text = text.lower()
    character_count={}
    for character in text:
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def sort_dict_by_value(dictionary):
    dic = list(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    #dic = list(dic.items())
    return dic