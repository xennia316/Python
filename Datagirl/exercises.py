# Exercise 1
import random
from operator import indexOf
from tokenize import String


a_list = [1, 2, 3, 4, 5]
print(type(a_list))

print("The sum of this list is:", sum(a_list[:]))
print('\n')
print('______________________________________________')
print('Exercise 2')
print('______________________________________________')
print('\n')


def multiplier(lists):
    result = 1
    for num in lists:
        result *= num
    return result


print(multiplier(a_list))
print('\n')
print('______________________________________________')
print('Exercise 3')
print('______________________________________________')
print('\n')

listing = [2, 3, 1, 20, 0]


def greatest(arg):
    result = 0
    for num in arg:
        if(num > result):
            result = num
    return result


print(greatest(listing))
print('\n')
print('______________________________________________')
print('Exercise 4')
print('______________________________________________')
print('\n')


def least(arg):
    result = 0
    for num in arg:
        if(num < result):
            result = num
    return result


print(least(listing))
