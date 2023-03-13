# import array as arr
# arr.array() we can use second method to get all element of an array

from array import *

vals = array('i', [1, 2, 3])  # there is other codes like i

'''
Type code : 'b' , C Type : signed char, Python type : int, min size in bytes : 1
Type code : 'B' , C Type : unsigned char, Python type : int, min size in bytes : 1
Type code : 'u' , C Type : Py_UNICODE, Python type : Unicode Character, min size in bytes : 2
Type code : 'h' , C Type : signed short, Python type : int, min size in bytes : 2
Type code : 'H' , C Type : unsigned short, Python type : int, min size in bytes : 2
Type code : 'i' , C Type : signed int, Python type : int, min size in bytes : 2
Type code : 'I' , C Type : unsigned int, Python type : int, min size in bytes : 2
Type code : 'l' , C Type : signed long, Python type : int, min size in bytes : 4
Type code : 'L' , C Type : unsigned long, Python type : int, min size in bytes : 4
Type code : 'f' , C Type : float, Python type : float, min size in bytes : 4
Type code : 'd' , C Type : double, Python type : float, min size in bytes : 4
'''
# Unsigned means positive value till particular value

vals = array('i', [1, 2, 3, 4])

# buffer info returns (address of value, size of value)
print(vals.buffer_info())
print(vals.typecode)
# there are plenty of method like this in array you can see with the help of pressing ctrl + space after dot
vals.reverse()
print(vals)
vals.reverse()

# You can also use indexing like list with the help of index number

# You can also iterate through array
for i in vals:
    print(i)
print()
# Second method
for i in range(len(vals)):
    print(vals[i])


'''if we want to copy array you can use comprehension'''

arr = array('i', [1, 2, 3, 4])
new_arr = array(arr.typecode, (a for a in vals))
# arr.typecode will simply compy type code from other array and a for a in vals take one by one value and assign
# to new array thats how new array will copy from old array

'''we can also print value of array using while loop'''
print()
counter = 0
while counter < len(new_arr):
    print(new_arr[counter])
    counter += 1

print()
print()
'''Question'''

# write a code to sort an array in ascending order
value_1 = array('i', [22, 11, 10, 90])
value_2 = array('i', [])
for i in range(len(arr)):
    minimum = min(value_1)
    value_2.insert(i, minimum)
    value_1.remove(minimum)

print(value_2)
