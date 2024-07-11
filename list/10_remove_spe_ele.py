def remover(lst):
    for i in range(len(lst)):
        if i==0 or i==4 or i==5:
            lst.pop(i)
    return lst

list=['a','b','c','d','e','f','g']
print(remover(list))