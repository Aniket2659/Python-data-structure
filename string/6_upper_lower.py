def upper_lower_case(string):
    up=string.upper()
    low=string.lower()
    return up,low
string=input("Enter a string :")
up,low=upper_lower_case(string)
print(f'upper case word = {up} and lower case word = {low}')    