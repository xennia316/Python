password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password

print(icecream, password)

# Creating new tuples with tuple() command
marx_list =[ 'hello', 'how', 'are', 'you']
tuple(marx_list)

# Combining two or more tuples with +
('hello') + ('how', 'are', 'you')

marx_list + ('doing')

print(marx_list)

#Duplicating items with *
mangoes = ('mango') * 3
print(mangoes) 

# Comparing Tuples with == sign. Returns true or false
a = (7, 2)
b = 7, 2, 9

print(a == b) #false

print(a <= b) #true

print(a < b) #true

print(a > b) #false

#Iterating with  for...in

words = 'fresh', 'fish'

for word in words:
    print(word)

# Modifying a tuple is some how impossible since tuples are immutable.
# Other methods could be adopted such as adding (+) etc
