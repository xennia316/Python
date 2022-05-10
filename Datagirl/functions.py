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


def print_args(*args):
    print('Positional tuple:', args)


print(print_args(3, 2, 1, 'wait!', 'uh...'))
