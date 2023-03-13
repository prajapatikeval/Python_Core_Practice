import sys

print(sys.getrecursionlimit())
# recursion limit is by default 1000

''' you can increase the recursion limit'''
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0


def greet():
    global i
    print(i, "Hello")
    i += 1
    greet()


greet()
