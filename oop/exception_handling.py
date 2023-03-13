a = 10
b = 0


try:
    print("Resource open")
    print(a/b)
except Exception as e:
    print("Hey, you can not divide number by zero", e)
finally:
    print("Resource closed")


'''for different type of error we have different exception and this Exception take all the error'''

try:
    print("resource open")
    print(a/b)
    u = int(input("Enter a number :"))
except ZeroDivisionError as e:
    print("Hey, you can not divide number by zero", e)
except ValueError as e:
    print("Invalid input")
except Exception as e:
    print("Something went wrong.. ", e)
finally:
    print("Resource closed")
