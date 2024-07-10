
def last_part(string,spe_char):
    for i in string[::-1]:
        if i==spe_char:
            return string[string[::-1].index(i):]
string=input('enter a string')
special_char=input(f'enter a special char in {string} :')

print(f'last part is {last_part(string,special_char)}')
    
