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

# Finding values in a set

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# Which drinks contain vodka?

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

    elif 'vermouth' in contents:
        print(f'vermouth in', name)

# Intersection &
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

# Rewriting the above...
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

print(a & b)
print(a.intersection(b))
