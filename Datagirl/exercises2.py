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
print('Exercise 3')
print('________________________')


def show_employee(name, salary=9000):
    print('Name: ', name + '\n' + 'Salary: ', salary)
    print('\n')


show_employee("Ben", 12000)
show_employee("Jessa")
