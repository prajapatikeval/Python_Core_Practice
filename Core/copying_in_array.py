from numpy import *

arr = array([1, 2, 3, 4, 5])
'''add value 5 in each element'''
k = 0
for i in arr:
    arr[k] = i + 5
    k += 1

'''or simply we can use this method'''

arr = arr+5

'''you can also add two array in one its also called as vectorized operation'''
arr = array([1, 2, 3, 4, 5])
arr1 = array([1, 2, 3, 4, 5])
arr3 = arr + arr1
print(arr3)

# You can also different method of mathematics in numpy
print(sin(arr))  # etc

# you can also concatenate two array

arr1 = array([1, 2, 3, 4])
arr2 = array([5, 6, 7, 8])
arr3 = concatenate([arr1, arr2])
print(arr3)

# Copying an array

'''shallow copy'''
arr1 = array([1, 2, 3, 4])
# view is function to help to copy a array and store array in different address
arr2 = arr1.view()
print(id(arr1))
print(id(arr2))

'''Deep copy'''

arr2 = arr1.copy()
print(id(arr2))

'''Questions'''

# first : write a code to add 2 arrays using forloop

value_1 = array([1, 2, 3, 4])
value_2 = array([1, 1, 1, 1])
k = 0
ans = ([])
for value in value_1:
    value_3 = value + value_2[k]
    ans.append(value_3)

print(ans)

# second : write a code to find maximum value from an array without using pre-built function

arr_1 = array([1, 2, 3, 10, 5])

ans = 0
for i in range(len(arr_1)):
    for j in range(i+1, len(arr_1)):
        if arr_1[i] > arr_1[j]:
            ans = arr_1[i]

print("The maximum value is :", ans)
