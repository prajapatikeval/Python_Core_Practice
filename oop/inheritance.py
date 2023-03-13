class A:  # A is super/parent class of B
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):  # B is a child\sub class of A, B is inheriting all the feature of class A
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(B):  # it's called multilevel inheritance
    def feature5(self):
        print("Feature 5 working")


'''we also have multiple inheritance'''


class AB:
    def feature1(self):
        print("Feature1")


class BC:
    def feature2(self):
        print("Feature2")


class CC(AB, BC):  # it's called as multiple inheritance
    def feature3(self):
        print("feature3")


a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature1()
cc = CC()
cc.feature1()
