
def fact(value):
    result = 1
    for i in range(1, value+1):
        result *= i
    return result


value = 5
result = fact(value)
print(result)
