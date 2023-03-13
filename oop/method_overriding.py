class A:
    def show(self):
        print("In A show")


class B:
    def show(self):  # You can see we are overriding a method
        print("In B show")


s1 = B()
s1.show()
