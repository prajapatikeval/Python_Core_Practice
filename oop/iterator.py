list = [1, 2, 3, 4]
# first way
'''print(list[0])
'''
# second way
'''for i in list:
    print(i)
'''
# third way
'''it = iter(list)
print(it.__next__())
print(it.__next__())
print(next(it)) #both are same
'''


'''Lets create our own iterator'''


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration  # it will raise an error and stop it


values = TopTen()
print(next(values))
for i in values:
    print(i)
