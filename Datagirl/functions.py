# Defining a function withh def keyword

def do_nothing():
    pass


do_nothing()


def make_a_sound():
    print("***************")
    print('quack')
    print("***************")


make_a_sound()

# Function with no parameter and a return value


def agree():
    return True


if agree():
    print('Splendid')
else:
    print('That was unexpected!')

# Function with parameters


def echo(anything):
    return anything + ' ' + anything


print(echo('Sally'))


def commentary(color):
    if color == 'red':
        return 'It\'s a tomato.'
    elif color == 'green':
        return 'It\'s a green pepper'
    elif color == 'bee purple':
        return 'I don\'t know what it is, but bees can definitely see it'
    else:
        return 'I\'ve never heard of the color ' + color + '.'


print(commentary('white'))

"""None is a special Python value that holds a place when there is nothing to say. It is
not the same as the boolean value False, although it looks false when evaluated as
a boolean. Here’s an example:"""

thing = None
if thing:
    print("I am something")
else:
    print("I am nothing")


def whatis(thing):
    if thing is None:
        print(thing, 'is None')
    elif thing:
        print(thing, 'is True')
    else:
        print(thing, 'is False')


whatis('Nice')
whatis(None)
whatis(True)

# Positional Arguments


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken', 'cake'))

# Keyword Arguments
print(menu(entree='beef', dessert='bagel', wine='bordeaux')
      )

# Mixture of position and keyword arguments
print(menu('frontenac', dessert='flan', entree='fish'))

# Default arguments


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('chardonnay', 'chicken')
      )

print(menu('dunkelfelder', 'duck', 'doughnut'))


# Explode/Gather Positional Arguments with *
def print_args(*args):
    print('Positional tuple:', args)


print(print_args(3, 2, 1, 'wait!', 'uh  '))


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)


(print_more('cap', 'gloves', 'scarf',  'monocle', 'mustache wax'))

# Explode/Gather Keyword Arguments with **


def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# Keyword-Only Arguments


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']
print('*************************')
print_data(data)
print('*************************')
print_data(data, start=3)
print('*************************')
print_data(data, end=2)

# Mutable and immutable arguments
outside = ['one', 'fine', 'day']


def mangle(arg):
    arg[1] = 'terrible!'


print('\n')
print(outside)
print('\n')
mangle(outside)
print('\n')
print(outside)


# Functions as first class citizens
def answer():
    print(42)


def run_something(func):
    func()


run_something(answer)
print(type(run_something))


def add_args(arg1, arg2):
    print(arg1 + arg2)


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


print(run_with_positional_args(sum_args, 1, 2, 3, 4))

# Inner functions


def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)


print(outer(4, 7))


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)


print(knights('Ni!'))

# Functions as closure


def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2


a = knights2('Duck')
b = knights2('Hasenpfeffer')

print(type(a))
print(type(b))

print((a))
print((b))

print((a()))
print((b()))
