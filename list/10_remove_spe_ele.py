def remover(lst):
    new=[]
    for i in range(len(lst)):
        if i!=0 and i!=3 and i!=4:
            new.append(lst[i])
    return new

list=['a','b','c','d','e','f','g']
print(remover(list))