# Create with []
from ntpath import join


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

# Join is the opposite of split
seperator = '*'
friends = ['Sally', 'Edwin', 'Sonia', 'Acha']
joined = seperator.join(friends)

print(joined)

seperated = joined.split(seperator)
print(seperated)

print(seperated == joined)

# Sorting lists with sort()
print(marxes.sort())
# Sorts lists in alphabetic order by default and numbers in ascending order

sorted(marxes) #Also sorts lists in alphabetical order or ascending order for strings and numbers respectively.

# *******************************************************************************************

# Sorted returns the  sorted list but sort does not
# Sorted does not change the original list but sort does

# *******************************************************************************************

# Reversing the sorting order

marxes.sort(reverse = True)
print(marxes)

# Finding list length

print(len(marxes))

# Assign with '='

a = [1 , 2, 3]
print(a) # [1, 2, 3]

b = a
print(b) #[1, 2, 3]

a[0] = 'I changed'

print(b) # ['I changed', 2, 3]

# Both a and b are pointing to thesame object location in memory

# Copying a list

a = [1, 2, 3]
b = a.copy()

print(a) # [1, 2, 3]
print(b)  # [1, 2, 3]

b[0] = 'Copied version'
print(a) #[1, 2, 3]

# List method for copying list

c = list(a)

print(a) # [1, 2, 3]
print(c)  # [1, 2, 3]

c[0] = 'New copied version'
print(a) #[1, 2, 3]

# Copying with slice method

d = a[:]

print(a) # [1, 2, 3]
print(d)  # [1, 2, 3]

d[0] = 'Newest copied version'
print(a) #[1, 2, 3]

#********************************************************************************************************************************************

# Copying with the copy, list() and slice method do not alter the original list whereas the direct assignment method alters the original list

#********************************************************************************************************************************************

# Deep copy
import copy

a = [1, 2[8, 9]]

b = copy.deepcopy(a)

# Comparing lists. You can directly compare two lists with the comparison methods like ==, < , > etc

a = [2, 3, 4]
b = [ 1, 2, 3]

a == b 
# Returns false