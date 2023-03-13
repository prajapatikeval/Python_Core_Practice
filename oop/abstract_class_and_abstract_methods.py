from abc import ABC, abstractmethod


'''It's not a abstract class and method'''


class Computer:
    def process(self):
        pass


com = Computer()  # you can not create a object of abstract class


'''abstract class and method'''


class Comp(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Comp):
    def process(self):
        print("It's running")


class Whiteboard:
    def write(self):
        print("It's writing")


class Programmer:
    def work(self, com):
        print("Solving bugs")
        com.process()


com1 = Laptop()  # It will print an error
prog = Programmer()
# com1.process()
prog.work(com1)
