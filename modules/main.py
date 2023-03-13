# import calc
from calc import *

value1 = int(input("Enter first value : "))
mod = input("Enter * , + , - , / : ")
value2 = int(input("Enter second value : "))

if mod == '*':
    print(mul(value1, value2))
elif mod == '+':
    print(add(value1, value2))
elif mod == '-':
    print(sub(value1, value2))
elif mod == '/':
    print(div(value1, value2))
