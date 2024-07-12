def list_to_nested_dict(lst):
    nested_dict = {}
    current_level = nested_dict

    for item in lst:
        current_level[item] = {}
        current_level = current_level[item] 

    return nested_dict

my_list = ['a', 'b', 'c', 'd']
result = list_to_nested_dict(my_list)
print(result)
