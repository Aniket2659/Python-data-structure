import numpy as np

def remove_1st(arr,element):
    
    for i in arr:
        if i==element:
            ar=np.remove(i)
            break
    return ar

ar=np.array([1,2,3,4,5,5,4,7,5,6,4,5])
element=int(input('enter a specific elemet :'))
print(remove_1st(ar,element))