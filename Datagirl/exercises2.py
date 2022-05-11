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
