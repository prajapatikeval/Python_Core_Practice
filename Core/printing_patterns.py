''' #
    ##
    ###
    ####
    #####'''
for i in range(5):
    for j in range(i):
        print("#", end=" ")
    print()

print()
''' #####
    ####
    ###
    ##
    #'''
for i in range(5):
    for j in range(5-i):
        print("#", end=" ")
    print()

print()
'''Questions'''
'''First:
    1 2 3 4
    2 3 4
    3 4
    4'''

num = 1
for i in range(1, 5):
    for j in range(1, 6-i):
        print(num, end=" ")
        num += 1
    num = 1
    num += i
    print()

print()
'''Second : 
    A P Q R
    A B Q R
    A B C R
    A B C D'''

num2 = 80
for i in range(4):
    num = 65
    for j in range(4):
        if j <= i:
            print(chr(num), end=" ")
            num += 1
        else:
            print(chr(num2), end=" ")
            num2 += 1
    num2 = 80
    num2 += i+1
    print()
