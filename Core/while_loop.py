print("abc")
print("abc")
print("abc")
print("abc")
print("abc")

'''unless doing this do this'''
i = 1
while i <= 5:
    print("Hello")
    i += 1

'You can also decrement i'
i = 5
while i >= 1:
    print(i, "HELLO")
    i -= 1

print()
print()

'You can use while inside while'
i = 1
while i <= 5:
    print(i, "HELLO", end="")
    j = 1
    while j <= 4:
        print(" Rocks", end="")
        j += 1
    i += 1
    print()

# Questions

'First : write a code to print all the values from 1 to 100 skip the numbers which are divisable by 3 and 5'

start = 1
end = 100

while start <= 100:
    if start % 3 == 0 and start % 5 == 0:
        print(start, end=" ")
    start += 1

print()
print()

'''Second : print pattern 
    #####
    #####
    #####
    #####
    #####
'''

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print('#', end=" ")
        j += 1
    i += 1
    print()
