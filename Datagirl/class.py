from ast import Pass
from urllib.parse import ParseResultBytes


class Cat():
    Pass

a_cat =  Cat()
another_cat = Cat()

print(type(Cat))
print(type(1))

a_cat.name = "Sonia"

print(a_cat.name)
print(a_cat)