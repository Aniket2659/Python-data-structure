def find_longer_word(lst,n):
    new=[]
    for i in lst:
        if len(i)>n:
            new.append(i)
    return new

list=input('enter :').split(',')
n=int(input('enter :'))
print(find_longer_word(list,n))
    