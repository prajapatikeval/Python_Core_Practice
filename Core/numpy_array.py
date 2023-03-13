from numpy import *

# six way to create an array
'''
array()
linspace()
logspace()
arrange()
zeros()
ones()
'''

# we dont need to specify the array type like we do in python it just automatically set
arr = array([1, 2, 3, 4, 5])
# you can also check a type of an array with the help of arr.dtype

arra = linspace(0, 15)  # the range between 0 15 is divided into 16 parts

arr = arange(1, 15, 2)  # its not an arange its an a range
# its same as range

# in log space it don't divide a value in same space it will divide value upon log of it
arr = logspace(1, 40, 5)

# it will by default create an array with 0 in range of given value in brackets by default it will be float
# you can also change the type of array by using second parameter
arr = zeros(10, int)

# same like zero but it will create array with value one
arr = ones(10)
