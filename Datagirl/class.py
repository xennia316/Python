

class Cat():
    pass


a_cat = Cat()
another_cat = Cat()

print(type(Cat))
print(type(1))

a_cat.name = "Sonia"

print(a_cat.name)


class NewCat():
    def __init__(self, name):
        self.name = name


a_NewCat = NewCat("Edwin")

print(a_NewCat.name)


class Car():
    def exclaim(self):
        print("I am a car!")


class Yoga(Car):
    pass


a_yoga = Yoga()
a_yoga.exclaim()


class Person:
    def __init__(self, name):
        self.name = name


class Medical_doctor(Person):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name + " is a doctor")


Edwin = Medical_doctor()
print(Edwin.name)
