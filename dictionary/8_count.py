def create_char_dict(input_string):
    char_dict = {}
    for char in input_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

input_string = "w3resource"
print(create_char_dict(input_string))
