def counting_char(string):
    dict={}
    for i in string:
        dict[i]=string.count(i)
    return dict

given_string=input('enter a string :')
print(counting_char(given_string))