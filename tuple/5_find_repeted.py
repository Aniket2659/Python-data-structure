def find_rep(tup):
    lst=[]
    for i in range(len(tup)):
        for j in range(i+1,len(tup)):
            if tup[i]==tup[j]:
                lst.append(tup[i])
    return lst
tpl=(1,2,3,4,5,65,4,2)
print(find_rep(tpl))