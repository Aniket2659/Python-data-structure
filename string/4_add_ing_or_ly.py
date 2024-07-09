def add(string):
    if len(string)>=3 and string[-3:]!='ing':
        return string +'ing'
    elif len(string)>=3 and string[-3:]=='ing':
        return string +'ly'
    else:
        return string
given_string=input('enter the string :')
print(add(given_string))

