from array import *

arr = array('i', [])

array_size = int(input("Enter the length of an array : "))

for i in range(array_size):
    user_input = int(input(f"Enter the value number {i+1}: "))
    arr.append(user_input)

print(arr)
search = int(input("Enter a value to search : "))

i = 0
while i < array_size:
    if search == arr[i]:
        print("Element found on index number :", i)
        break
    i += 1
else:
    print("Element not found")

'''You can also use for loop'''

for i in range(array_size):
    if search == arr[i]:
        print("Element found on index number :", i)
        break
else:
    print("Element not found")

'''second method'''
k = 0
for value in arr:
    if value == search:
        print("Element found on index number :", k)
        break
    k += 1
else:
    print("Element not found")


'''we can also use function to search index of element'''

print("Element found on index number :", arr.index(search))


'''Question'''
# First : create an array with 5 values & delete the value at index no : 2 with out using in_built function

arr = array('i', [])
array_size = 5

for i in range(array_size):
    value = int(input(f"Enter a value number {i}: "))
    arr.append(value)

index_to_delete = 2
print(f"Before deleting index number {index_to_delete} :", arr)

for i in range(array_size):
    if i == index_to_delete:
        arr.remove(arr[i])

print(f"After deleting index number {index_to_delete} :", arr)

# Second : write a code to reverse an array with out using built-in function

arr = array('i', [1, 2, 3])
new_arr = array('i', [])
print(f"Before reversing an array : {arr}")
i = len(arr)-1
k = 0
while k < len(arr):
    new_arr.insert(k, arr[i])
    k += 1
    i -= 1
print(f"after reversing an array : {new_arr}")
