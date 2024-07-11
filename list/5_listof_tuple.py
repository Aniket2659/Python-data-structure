def sorting_tup(tup):
    n=len(tup)
    for i in range(n):
        for j in range(0,n-i-1):
            if tup[j][-1]>tup[j+1][-1]:
                tup[j],tup[j+1]=tup[j+1],tup[j]
    return tup

Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorting_tup(Sample_List))