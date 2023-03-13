# instance variable

class Car:
    def __init__(self):
        self.mil = 10  # this called instance variable it stored in instance namespace
        self.com = 'BMW'


c1 = Car()
c2 = Car()
c1.mil = 20  # you can change the value of particular object value like this
print(c1.mil, c1.com)
print(c2.mil, c2.com)

# class variable


class Car:
    Wheels = 4  # this called class variable you can say who has like particular fixed value

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()
print(c1.Wheels)
print(c2.Wheels)
Car.Wheels = 5  # in order to change class variable we need to use class it self to change the variable
# once it changes it apply to all other objects of a class
print(c1.Wheels)
print(c2.Wheels)
