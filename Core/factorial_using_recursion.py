
def fact(value):
    if value == 0:
        return 1
    return value * fact(value-1)


result = fact(4)
print(result)
