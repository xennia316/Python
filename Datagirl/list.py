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

# reversing a list

marxes.reverse() #reverses but returns nothing

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