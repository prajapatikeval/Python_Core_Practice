from numpy import *

arr = array([
    [1, 2, 3],
    [4, 5, 6]
])

# ndim function help to check the array is 1d or 2d in this case it returns 2 it means 2d
print(arr.ndim)
print(arr.shape)  # it will return type of array like 2x3 or 3x3

print(arr.size)  # it will return entire array size

'''you can also convert 2d array in 1d array'''

arr2 = arr.flatten()
print(arr2)

'''now 2d to 3d'''
arr = array([[1, 2, 3, 4, 5, 1], [6, 7, 8, 9, 0, 1]])
# it will create 2 2d array and in each 2d array we will have 2 1d array and each will have 3 value
arr3 = arr.reshape(2, 2, 3)
print(arr3)


'''matrix operations'''

# arr = array([[1, 2, 3, 4], [6, 7, 8, 9]])
# this one way of doing this

# second is
# semicolon represent as a how many row or after semicolon the value will be in new line
m = matrix('1 2 3; 4 4 5; 6 7 1')
m1 = matrix('1 2 1; 4 4 1; 2 1 1')

'if you want to get diagonal value like maths matrices '
print(diagonal(m))
print(m.min())  # minimum

'''You can addition or multiply two matrices in python'''

m3 = m + m1
m4 = m * m1
print(m3, "\n", m4)
