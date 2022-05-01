# Create with []
empty_list = []
week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]

# Converting other datatypes to list with list()
another_empty_list = list()

print(another_empty_list)

list('cats')

# Creating a string with split
talk_like_a_pirate_day = '9/19/2019'
talk_like_a_pirate_day.split('/')

print(talk_like_a_pirate_day.split('/'))
#['9', '19', '2019']

#Get an Item by [ offset ]
#As with strings, you can extract a single value from a list by specifying its offset:
marxes = ['Groucho', 'Chico', 'Harpo']

marxes[0]
 #'Groucho'
marxes[1]
 #'Chico'
marxes[2]
 #'Harpo'

#Again, as with strings, negative indexes count backward from the end:
marxes[-1]
 #'Harpo'
marxes[-2]
 #'Chico'
marxes[-3]
 #'Groucho'

#  Slicing elements of a list

print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])

# Reversing a list

marxes.reverse() #Reverses but returns nothing

# Appending elements to the end of a list
marxes.append('Zepppo')

# Inserting st any offset position
marxes.insert(2, 'Gummo')
print(marxes)

# Duplicating a lists elements
['blah'] * 3
#['blah', 'blah', 'blah']

# Combine Lists by Using extend() or +
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)

print(marxes)
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

# Alternatively, you can use + or +=:
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others

print(marxes)
#['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

# Changing the value at an offset position
marxes[2] = 'Wanda'

# Change Items with a Slice

# The previous section showed how to get a sublist with a slice. You can also assign
# values to a sublist with a slice:
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]

print(numbers)

# Deleting with del

del marxes [-1]
# The previous line will delete Karl

# Deletion could also be done with remove()

marxes.remove('Groucho') #This will equally delete Groucho from the list
# The above method is suitable when the exact index is not known

# Deleting with pop and offset position
# Poping with an offset returns the item at that offset

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()
#  returns 'Zeppo' because pop has a default offsset of -1
print(marxes)

marxes.pop(1)
'Chico'
print(marxes)

# If you want to know the offset of an item in a list by its value, use index():
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico')
# The above line returns 1

# If the value is in the list more than once, only the offset of the first one is returned:
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

# To count how many times a particular value occurs in a list, use count():

marxes = ['Groucho', 'Chico', 'Harpo', 'Harpo']
marxes.count('Harpo')

# Convert a list to a string with 'join'

' '.join(marxes)
# Returns 'Groucho Chico Harpo Harpo'

