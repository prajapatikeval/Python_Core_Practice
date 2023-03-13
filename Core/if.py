if False:
    print("Hello")
print("Bye")

''''''
x = 3
r = x % 2
if r == 0:
    print(x, "is Even")
if r == 1:
    print(x, "is odd")

'''Second method'''
x = 8
if x % 2 == 0:
    print(x, "is Even")
if x % 2 == 1:
    print(x, "is odd")

'''Now if first condition is true and you don't want to check second condition than we use else'''
x = 10
if x % 2 == 0:
    print(x, "is evan")
    if x > 5:
        print("Great")
    else:
        print("Not Great")
else:
    print(x, "is odd")


'''Elif in if else'''

x = 1
if x == 1:
    print("One")
elif x == 2:
    print("Two")
else:
    print("Another number")


#  Questions of if else

'First : write a code to check a given number is positive or negative'

number = int(input("Enter a number positive or negative: "))
if number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is zero")
else:
    print("Number is positive")

'Second : Take three values from user and find the gretest number'
'''First method'''
first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter third number : "))

if first_number > second_number and first_number > third_number:
    print(first_number, " is greater")
elif second_number > third_number and second_number > first_number:
    print(second_number, "is greater")
else:
    print(third_number, "is greater")

'''Second method'''

first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter third number : "))

list = [first_number, second_number, third_number]
print(max(list), "is greater")
