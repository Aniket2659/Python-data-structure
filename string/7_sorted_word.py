def sorting(lst):
    unique_lst=set(lst)
    final_list=sorted(unique_lst)
    return ', '.join(final_list)

words = input("Enter a comma separated sequence of words: ").strip().split(',')

print(sorting(words))