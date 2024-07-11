def split_list_by_first_char(lst):
    list1=[]
    list2=[]
    list3=[]
    first_letter=[]
    for i in range(len(lst)):
        if lst[i][0] not in first_letter:
            first_letter.append(lst[i][0])
    for j in range(len(lst)):
        if first_letter[0] == lst[j][0]:
            list1.append(lst[j])
    for k in range(len(lst)):
        if first_letter[1] == lst[k][0]:
            list2.append(lst[k])
    for l in range(len(lst)):
        if first_letter[2] == lst[l][0]:
            list3.append(lst[l])


        
    return [list1,list2,list3]
list=['aniket','babar','anar','banana','cat']
print(split_list_by_first_char(list))
