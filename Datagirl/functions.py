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
