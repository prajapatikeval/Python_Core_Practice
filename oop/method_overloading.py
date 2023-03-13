class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # def sum(self, a=None, b=None, c=None):
    #     s = 0
    #     if a != None and b != None and c != None:
    #         s = a+b+c
    #     elif a != None and b != None:
    #         s = a+b
    #     else:
    #         s = a
    #     return s Instead of this use this

    def sum(self, *data):  # you can use positional argument
        s = 0
        for i in data:
            s = s+i
        return s

    # def sum(self, a, b):
    #     s = a+b
    #     return s
    # we can not do in python


s1 = Student(10, 20)
print(s1.sum())
