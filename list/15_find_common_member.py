def find_common(lst1,lst2):
    new=[]
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i]==lst2[j]:
                new.append(lst1[i])
                return lst1
            
list1=[1,2,3,4,5]
list2=[4,2,1,5,6]
print(find_common(list1,list2))