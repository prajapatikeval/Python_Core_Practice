av = 4
x = int(input("How many candy you want? : "))
i = 1

while i <= x:
    if i > av:
        print("Sorry! Candy out of stock! we don't have",
              x, "Candy our stock is only", av)
        break
    else:
        print(i, "Candy")
    i += 1
print("Thank you for coming")


'''Continue'''

for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)
print("Thank you for coming")


'''pass'''
for i in range(1, 11):
    if i % 2 != 0:
        pass
    else:
        print(i)
print("Thank you for coming")


'''Question'''

# First : print first 50 fibonacci numbers.

a, b = 0, 1
sum = 0
for _ in range(1, 51):
    print(a)
    sum = a+b
    a = b
    b = sum

# Second : check a given number is prime or not

input = int(input("Enter a number : "))

flag = False
if input == 1:
    print(input, "is not a prime number")
elif input > 1:
    for i in range(2, input):
        if input % i == 0:
            flag = True
            break
    # if flag == False:
    #     print(input, "is a prime number")
    # or
    if flag:
        print(input, "is not a prime number")
    else:
        print(input, "is a prime number")
