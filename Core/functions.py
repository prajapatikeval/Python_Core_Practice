def greet():
    print("Hello! good morning")


greet()

'''addition of two number using function'''


def addition(a, b):
    print(a+b)


addition(2, 3)


'''another type of function who can give you return a value'''


def multiply(a, b):
    return a*b


print(multiply(2, 2))

# you can also return two value at same time


def add_sub(a, b):
    return a+b, a-b


ans, ans1 = add_sub(5, 3)
print(ans, ans1)
