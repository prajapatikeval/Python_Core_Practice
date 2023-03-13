# we have different mode like r you can visit python documentation r means read
file = open('file_handling/data.txt', 'r')
print(file.readline(), end="")  # we also have method like read
print(file.readline())
file.close()
# in this method you need to manually close the file

'''write a data'''

# it will first check there is file or not if there is file then it will first clear file as we open it
# and write, if we don't have file then it will create new one
# if you don't want to loss data than use append(a) mode
file = open("file_handling/dta.txt", 'w')
file.write("writing first file using python")
file.close()


'''copy from one file to another'''
f = open('file_handling/data.txt')  # by default it is read
file = open("file_handling/copy.txt", 'w')
for data in f:
    file.write(data)
file.close()
f.close()

# in this method if you by mistake forget to close file you might loss data or get an error
# thats why we have second way to open file

with open('file_handling/data.txt')as file:
    with open('file_handling/copy.txt', 'w')as file1:
        for data in file:
            file1.write(data)

'''you can also print data of an image/ or just copy it'''

# we have two different type of mode one is character and second is binary
f = open('file_handling/Constructor.PNG', 'rb')
f1 = open('file_handling/Copy.JPG', 'wb')
for data in f:
    f1.write(data)
f1.close()
f.close()
