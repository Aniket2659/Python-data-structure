def remove(tup):
    tup=list(tup)
    tup.remove(tup[num])
    return tuple(tup)

tup=(1,2,3,4,5)
num=0
print(remove(tup))