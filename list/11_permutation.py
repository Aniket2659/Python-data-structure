def permutations(elements):
    if len(elements) == 1:
        return [elements]

    all_perms = []
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        
        for perm in permutations(remaining_elements):
            all_perms.append([current_element] + perm)

    return all_perms

my_list = [1, 2, 3]
permutations = permutations(my_list)
print(permutations)

