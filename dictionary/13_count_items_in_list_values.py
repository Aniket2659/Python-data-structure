def count_items_in_list_values(my_dict):
    total_count = 0
    for value in my_dict.values():
        if isinstance(value, list):  
            total_count += len(value)  
    return total_count

my_dict = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'potato'],
    'grains': 'rice',
    'dairy': ['milk', 'cheese', 'yogurt']
}

count = count_items_in_list_values(my_dict)
print("Total number of items in list values:", count)
