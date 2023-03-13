class Student:
    school = 'public'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):  # This is called a getters to get the value
        return self.m1

    def set_m1(self, value):  # This is called setters to set a particular value
        self.m1 = value

    @classmethod  # It called decorator we wil talk about later if we need to use class method than we need to use decorator
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class.. in abc module")


s1 = Student(10, 20, 30)
s2 = Student(20, 30, 40)
print(s1.avg())
print(s2.avg())
print(Student.getSchool())

Student.info()
