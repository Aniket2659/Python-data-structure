def longest_word(li):
    max=len(li[0])
    for i in range(1,len(li)):
        if len(li[i])>max:
            max=len(li[i])
    for j in li:
        if len(j)==max:
            a=j
    return j

given_li=['aniket','babar','ram','aakashhh']
print(longest_word(given_li))
