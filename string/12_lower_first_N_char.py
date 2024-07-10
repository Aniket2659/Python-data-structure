def lower(string,N):
    return (string[0 : (N)].lower())+string[N:]
string=input('enter string :')
num=int(input('enter number :'))
print(f'first {num} leters {string} converted into lower case :{lower(string,num)} ')

