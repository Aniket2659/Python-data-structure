import re
string='hii my name is aniket and i am from satara and you'
substring='and'
store=re.findall(substring,string)
print(len(store))
    