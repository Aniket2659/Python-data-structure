def update(string):
    update_string=string[0]+(string[1:].replace(string[0],'$'))
    return update_string
given_string=input('enter a string :')
print(update(given_string))