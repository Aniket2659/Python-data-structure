def iscircular(lst1,lst2):
    if lst1==lst2[::-1]:
        return True
    
list1=[1,2,3,4]
list2=[4,3,2,1]
print(iscircular(list1,list2))