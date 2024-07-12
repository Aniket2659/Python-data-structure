def print_dict_table(my_dict):
    print(f"{'Key            '} {'Value'}")
    print("-" * 30)
    for key, value in my_dict.items():
        print(f"{key}             {value}")
              
my_dict = {'apple': 3, 'banana': 2, 'cherry': 5, 'date': 4}
print_dict_table(my_dict)
