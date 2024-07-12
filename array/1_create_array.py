import numpy as np

def creation(arr):
    for i in range(5):
        num=int(input('enter a element :'))
        arr=np.append(arr,num)
    return type(arr)

ar=np.array([],dtype=int)
print(creation(ar))