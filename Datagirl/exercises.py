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
print('\n')
print('______________________________________________')
print('Exercise 7')
print('______________________________________________')
print('\n')

my_list = [1, 2, 3, 4, 1, 2, 5]
new_list = dict.fromkeys(my_list)
print(list(new_list))

print('\n')
print('______________________________________________')
print('Exercise 8')
print('______________________________________________')
print('\n')


def checker(params):
    if(len(params) == 0):
        print("I am an empty list")
    else:
        print("Hello from a packed with %f elements", float(len(params)))


checker(sample_list)

print('\n')
print('______________________________________________')
print('Exercise 9')
print('______________________________________________')
print('\n')


def cloner(params):
    newList = params.copy()
    return newList


print('\n')
print('______________________________________________')
print('Exercise 10')
print('______________________________________________')
print('\n')

words = ['hello', 'there', 'me', 'you']


def inside(params):
    n = 3
    final_list = []
    for word in params:
        if(len(word) > n):
            final_list.append(word)
    return final_list


print(inside(words))
print('\n')
print('______________________________________________')
print('Exercise 11')
print('______________________________________________')
print('\n')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [0, 2, 4, 6, 8]


def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    print(result)
    return True


print(common_elements(list1, list2))

print('\n')
print('______________________________________________')
print('Exercise 12')
print('______________________________________________')
print('\n')


def deleter(params):
    first = params[0]
    second = params[4]
    third = params[5]

    params.remove(first)
    params.remove(second)
    params.remove(third)

    return params


print(deleter(my_list))


print('\n')
print('______________________________________________')
print('Exercise 13')
print('______________________________________________')
print('\n')


def remover(list):
    for elem in list:
        if elem % 2 == 0:
            list.remove(elem)
    return list


print("New list after removing all even numbers: ")
print(remover(my_list))
print('\n')
print('______________________________________________')
print('Exercise 14')
print('______________________________________________')
print('\n')


(random.shuffle(my_list))
print(my_list)

print('\n')
print('______________________________________________')
print('Exercise 15')
print('______________________________________________')
print('\n')

numbers = [1, 2, 3, 4, 5]


def swapper(list):
    first = list[0]
    last = list[-1]

    list[-1] = first
    list[0] = last

    return list


print(swapper(numbers))
