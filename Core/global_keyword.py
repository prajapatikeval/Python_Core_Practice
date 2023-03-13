a = 10  # global variable
# we can use global variable inside function etc as well as outside of it


def something():
    a = 1  # local variable
    # we can only use local variable in a function, loop etc not outside of it
    b = 10
    print("Inside function ", a)


# print(b) this will give you an error because it created for only something() function
something()
print("Outside function", a)
print()

'''if you want to change value of global variable from inside a loop or function'''
# we can use global

a = 10


def something():
    global a  # it will tell python to use global variable not to create another local variable
    a = 15
    print("Inside", a)


something()
print("Outside", a)
print()

'''If you want to use global and local variable in function at a same time'''

a = 10
b = 20


def something():
    a = 9
    # x = globals()  # it will give all global variable
    # for one we will use
    x = globals()['a']
    print("global x", x, "and local a ", a)
    print(id(x))
    # if we want to change global variable a value without affecting local variable
    globals()['a'] = 100


print("global a", a)
print(id(a))
something()
print("After changing value of a", a)
