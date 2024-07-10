def multi(list):
    multi=1
    for i in range(len(list)):
        multi=multi*list[i]
    return multi

lst=list(map(int,input('enter :').split(',')))
print(f'the multiplication of element in list is :{multi(lst)}')
        