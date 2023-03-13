def update(lst):
    lst[1] = 24
    print(id(lst), lst)


lst = [10, 20, 30]
update(lst)
print(id(lst), lst)

'''actual argument'''

# position argument


def person(name, age):
    print(name, age)


person('keval', 21)

# instead of this do this keyword argument
person(age=21, name='keval')  # so we dont need to care about position


# default argument
def person(name, age=18):
    print(name, age)


# in this method if you dont pass a value than it will take default value from function
person('keval')

# variable length argument


def sum(a, *b):
    c = a
    for i in b:
        c += i
    print(c)


sum(5, 3, 2, 3)  # this come to help when you passing value is not fixed


# kwargs

def person(name, **data):
    print(name)

    for key, value in data.items():
        print(key, value)


# if we want to pass multiple vale with keyword we will use kwargs
person('xyz', age=20, city='avx', mob=1245)
