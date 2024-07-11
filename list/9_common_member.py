def common_member(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i==j:
                return True
    return False

list1=[1,2,3,4,5,6]
list2=[7,8,9]
print(common_member(list1,list2))

