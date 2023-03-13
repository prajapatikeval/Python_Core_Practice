def topten():
    yield 1
    yield 2
    yield 3
    yield 4


values = topten()
print(values.__next__())

for i in values:
    print(i)

print()
print()
'''Getting top ten square'''


def TopTen():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq  # it will not terminate the function like return and also it's a generator
        n += 1


value = TopTen()

for i in value:
    print(i)

'''when to use generator  : when you have thousands of file data and you want to fetch the data
    and you don't want to load all the data at that time you just want to fetch one by one data 
    you will use generator and iterator'''
