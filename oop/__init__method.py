class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is :", self.cpu, self.ram)


com1 = Computer('i3', 16)
com2 = Computer('Ryzen', 16)


com1.config()
com2.config()
