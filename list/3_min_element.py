def min(lst):
    min=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min:
            min=lst[i]
    return min

list=list(map(int,input('enter the element with(",") :').split(',')))
print(f'the minimum element n list is {min(list)}')