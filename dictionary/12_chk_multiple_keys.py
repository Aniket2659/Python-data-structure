def check_keys_exist(my_dict, keys):
    return all(key in my_dict for key in keys)

my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'country': 'USA'
}

keys_to_check = ['name', 'age', 'country']

if check_keys_exist(my_dict, keys_to_check):
    print("All keys exist in the dictionary.")
else:
    print("Some keys do not exist in the dictionary.")
