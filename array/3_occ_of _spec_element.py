import numpy as np

def occurence(arr,element):
    count=0
    for i in arr:
        if i==element:
            count=count+1
    return count

ar=np.array([1,2,3,4,5,5,4,7,5,6,4,5])
element=int(input('enter a specific elemet :'))
print(occurence(ar,element))