def get_difference(ls1,ls2):
    new=[]
    for i in ls1:
        for j in ls2:
            if i==j:
                ls1.remove(i)
    return ls1
                
ls1=['aniket','abc','def']
ls2=['babar','xyz','aniket']
print(get_difference(ls1,ls2))