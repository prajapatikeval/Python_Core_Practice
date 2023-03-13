from functools import reduce
'''def is_even(val):
    return val % 2 == 0

def update(val):
    return val * 2

def add_all(val1,val2):
    return val1+val2
    
lst = [2, 3, 1, 4, 19, 8, 12]
evens = list(filter(is_even, lst))
doubles = list(filter(update,evens))
sum = reduce(add_all,doubles)
print(evens)
'''
# filter is use to take 2 value one is function and second is iterable it's use to filter a particular thing
# instead of define a function we can use lambda
lst = [2, 3, 1, 4, 19, 8, 12]
evens = list(filter(lambda value: value % 2 == 0, lst))
# map is use to change the value from particular thing
# it also take two argument one is function and second is iterable
doubles = list(map(lambda value: value * 2, evens))
# reduce is also have two parameter function and iterable
# reduce two parameter at a time after sum of that value than it will go to next item in list
sum = reduce(lambda value1, value2: value1+value2, doubles)
print(evens, doubles, sum)
