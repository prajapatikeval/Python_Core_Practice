a = 5
b = 9

print(a+b)
# behind the scene + is calling add method in int class we have different method for different operators
print(int.__add__(a, b))


'''operator overloading'''


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # we are changing the predefined method, it's called overloading operator +
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):  # gt means grater than
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 > s2:
            return True
        else:
            return False

    def __eq__(self, other):  # eq means equal to
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1 == s2:
            return True
        else:
            return False

    def __str__(self):  # default str method print address of class
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(21, 29)
s2 = Student(9, 90)

s3 = s1+s2
print(s3.m1)
print(s3.m2)


if s1 > s2:
    print("S1 is greater")
elif s1 == s2:
    print("Both are equal")
else:
    print("s2 is greater")

print(s1, s2)
