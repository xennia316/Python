empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}

print(odd_numbers)

# Creating a set from a string .... It counts only one occurrence of a character
print(set('letters'))

# Converting a list to a set
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

# Converting a tuple to a set
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))

# When you give set() a dictionary, it uses only the keys:
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

# Set length with len()
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

# Throw another item into a set with the add() method:
s = set((1, 2, 3))
print(s)

s.add(4)
print(s)

# Deleting from a set by value
s.remove(2)
print(s)

# Iterating through a set with for...in

furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)
