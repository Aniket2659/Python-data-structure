def append_list(lst,ls2):
    for i in ls2:
        lst.append(i)
    return lst

list1=[1,2,3,4]
list2=[9,8,7,6]
print(append_list(list1,list2))