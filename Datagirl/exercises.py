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

print('\n')
print('______________________________________________')
print('Exercise 5')
print('______________________________________________')
print('\n')

Sample_List = ['abc', 'xyz', 'aba', '1221']


def counter(args):
    counting = 0
    for arg in args:
        if len(arg) > 2:
            # if type(arg) == 'String':
            if arg[0] == arg[-1]:
                counting += 1
    return counting


print(counter(Sample_List))

print('\n')
print('______________________________________________')
print('Exercise 6')
print('______________________________________________')
print('\n')

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def second(arg):
    return arg[1]


(sample_list.sort(key=second))
print(sample_list)
