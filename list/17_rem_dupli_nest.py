def remove_duplicates(lst):
    new=[]
    for i in range(len(lst)):
            if lst[i] not in new:

                new.append(lst[i])
                
    return new



Sample = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print(remove_duplicates(Sample))