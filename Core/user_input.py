import sys
import math

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = a+b
print(c)

''' Only fetching one character from string'''
# First method
ch = input("Enter a character : ")
print(ch[0])

# Second method
# This will fetch full string but stores only one character from the string
ch = input("Enter a character : ")[0]
print(ch)

'''Eval function'''
result = eval(input("Enter a expression : "))
print(result)  # it will evaluate a expression and give answer for example you enter
# 2 + 4 - 1 it will return 5


'''You can also get value from command prompt using argv(Argument values)'''
# a = int(sys.argv[1])  # Index number 0
# b = int(sys.argv[2])  # Index number 1

# index number 0 : file name , index number 1 : first expression, index number 2: second expression .... n

# print(a+b)


''' Practice question'''
# Write a code to find cube of the number Take the input from the user using input and also command line

v = int(input("Enter a number : "))
b = int(sys.argv[1])

print(int(math.pow(v, b)))
