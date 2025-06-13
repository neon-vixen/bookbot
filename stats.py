def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(text_string):
    words = text_string.split()
    return len(words)
    #Origional solution
    #word_count = len(text_string.split())
    #return word_count

def get_char_dict(text_string):
    char_dict = {}
    for char in text_string.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def get_sorted_dict(char_dict):
    dict_list =[]
    for key,value in char_dict.items():
        my_dict = {"letter": key, "count": value}
        dict_list.append(my_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["count"]