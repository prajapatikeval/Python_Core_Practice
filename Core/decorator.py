from functools import reduce


def div(val1, val2):
    if val1 < val2:
        val1, val2 = val2, val1
    print(val1/val2)


div(2, 4)
# if you dont want to change to function and what if you are importing the function from the another file
# you can use decorator


def div(val1, val2):
    return val1/val2


def smart_div(div):
    def inner(val1, val2):
        if val1 < val2:
            val1, val2 = val2, val1
        return div(val1, val2)
    return inner


result = smart_div(div)
print(result(2, 4))

'''Question sum a list without negative value'''


def sum(lst):
    return reduce(lambda value1, value2: value1+value2, lst)


def smart_div(sum):
    def inner(lst):
        for i in lst:
            if i < 0:
                lst.remove(i)
                continue
        return sum(lst)
    return inner


lst = [10, 20, 30, 40, -10000]
print(f"The sum of list: {lst} ", end="")
result = smart_div(sum)
print("is : {}".format(result(lst)))
