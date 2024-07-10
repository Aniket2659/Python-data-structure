def sum(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum
lst=list(map(int,input('enter :').split(',')))
print(f'the sum of element in list is :{sum(lst)}')
        