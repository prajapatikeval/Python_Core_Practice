class Computer:
    def config(self):  # this is a method(function) in oop we will say methods not functions
        # we will talk about self later
        print("i5 , 16gb, 1TB")


a = 'a'
print(type(a))  # you are using class from start
comp1 = Computer()
# and this is user defined class
# you can assign multiple object to a class like
comp2 = Computer()
comp3 = Computer()
print(type(comp1))
# you can say that every thing is object in python
# notice :  while creating class make sure not to use predefined class

# computer.config(comp1) instead of this we can use this
comp1.config()
