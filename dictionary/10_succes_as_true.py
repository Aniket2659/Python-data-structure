data = [
    {'id': 1, 'success': True, 'name': 'Lary'},
    {'id': 2, 'success': False, 'name': 'Rabi'},
    {'id': 3, 'success': True, 'name': 'Alex'}
]

def count_success_true(data):
    count = 0
    for item in data:
        if item.get('success') is True:
            count += 1
    return count
result = count_success_true(data)

print(f"Count of dictionaries with success as True {result}")
