class Student:  # outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # instance of laptop class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:  # inner class you can use this class on outer class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('keval', 20)
s2 = Student('keval2', 21)

s1.show()

# creating object of lap class

'''lap1 = s1.lap
lap2 = s2.lap
'''
# you can directly create an object of laptop class
lap1 = Student.Laptop()
