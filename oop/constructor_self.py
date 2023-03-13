class Computer:
    def __init__(self):
        self.name = "Keval"

    def update(self):
        self.name = "KEVAL"

    def compare(self, other):
        if self.name == other.name:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c1.name = "xyz"
c2.update()
print(c1.name)
print(c2.name)

if c1.compare(c2):
    print("They are same")
else:
    print("Not same")
