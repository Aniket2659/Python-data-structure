def find_string(lst):
    count=0
    for word in lst:
        if word[0]==word[-1] and len(word)>=2:
            count=count+1
    return count
        
lst=list(input('enter the element with quama sepereated :').split(','))
print(lst)
print(find_string(lst))
            
