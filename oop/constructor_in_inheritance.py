class A:
    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def __init__(self):  # While creating object of b it will first try to find init of sub class if not found than it will find super class init
        # super().__init__()  # with the help of this you can also call super class init also
        print("In B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()  # In this case we have two super class of C is A and B
        # and it will print super class A init
        # we have concept of MRO(Method Resolution Order) in multiple inheritance it start from left to right
        # and you can see while creating sub class of A and B,  A is first thats why A is calling first
        print("in C init")

    def feat(self):  # you can also called super class method using super() keyword
        super().feature3()


c1 = C()
c1.feat()
