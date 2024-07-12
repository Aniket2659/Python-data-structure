Sample = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_values = set()

for item in Sample:
    for key, value in item.items():
        unique_values.add(value)

my_dict = {i: value for i, value in enumerate(unique_values)}

print(my_dict)


