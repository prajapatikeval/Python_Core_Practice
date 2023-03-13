import calc
import calc2


def greet1():
    print("first function")
    calc2.add()


greet1()
print()
print()
'''with out __name__ you can see it will print whole main'''
# __name__ initial have __main__ value if you run from current file
# if you import module and pass __name__ than it will return module name
# __name__ is use to prevent running another file and use that file function without extra print
# when this variable have value main it means the main file is being executed not other


def greet2():
    print("second function")
    calc.add()


greet2()
