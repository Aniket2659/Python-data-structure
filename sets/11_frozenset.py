
sample_set = {1, 2, 3, 4, 5}

sample_set.add(6)
print("Mutable set after adding an element:", sample_set)

immutable_set = frozenset(sample_set)
print("Immutable frozenset:", immutable_set)

try:
    immutable_set.add(7)
except:
    print("Immutable set cannot be changed")

