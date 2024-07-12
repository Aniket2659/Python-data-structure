my_dict = {'apple': 3, 'banana': 2, 'cherry': 5, 'date': 4}

def get_value(item):
    return item[1]

ascending = dict(sorted(my_dict.items(), key=get_value))
descending = dict(sorted(my_dict.items(), key=get_value, reverse=True))

print(f"Original dictionary {my_dict}")
print(f"Dictionary sorted by value (ascending) {ascending}")
print(f"Dictionary sorted by value (descending) {descending}")
