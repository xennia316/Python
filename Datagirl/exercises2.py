import copy
from copy import deepcopy


print('________________________')
print('Exercise 1')
print('________________________')


def takes_two_args(name, age):
    print(name)
    print(age)


(takes_two_args('Sonia', 15))
print('________________________')
print('Exercise 2')
print('________________________')


def func1(*args):
    print(args)


func1(1, 2, 3, 4, 5, 'Nyenti')

print('________________________')
print('Exercise 3')
print('________________________')


def calculation(arg1, arg2):
    summed = arg1 + arg2
    reduced = arg1 - arg2
    return summed, reduced


print(calculation(20, 5))

print('________________________')
print('Exercise 4')
print('________________________')


def show_employee(name, salary=9000):
    print('Name: ', name + '\n' + 'Salary: ', salary)
    print('\n')


show_employee("Ben", 12000)
show_employee("Jessa")

print('________________________')
print('Exercise 5')
print('________________________')


def outer(a, b):
    def inner(a, b):
        return a + b
    return inner(a, b) + 5


print(outer(1, 2))

print('________________________')
print('Exercise 6')
print('________________________')


def summer(a):
    if a <= 1:
        return a
    else:
        return a + summer(a - 1)


print(summer(9))

print('________________________')
print('Exercise 7')
print('________________________')


def display_student(name, age):
    name = name
    age = age
    return name, age


def show_student(name, age):
    pass


show_student = copy.deepcopy(display_student)

print('________________________')
print('Exercise 8')
print('________________________')

for numbers in range(4, 31):
    if numbers % 2 == 0:
        print(numbers)

print('________________________')
print('Exercise 9')
print('________________________')


def largest(list):
    new_list = sorted(list)
    return new_list[-1]


random_list = [2, 3, 1, 7, 0, 9, 20]

print(largest(random_list))
