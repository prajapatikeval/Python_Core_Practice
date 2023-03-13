pos = 0


def Search(list, value):
    # i = 0
    # while i < len(list):
    #     if list[i] == value:
    #         # global pos
    #         # pos = i or
    #         globals()['pos'] = i + 1
    #         return True
    #     i += 1
    # return False
    # we can also do in while loop

    for data in list:
        if data == value:
            globals()['pos'] = list.index(value) + 1
            return True
    return False


list = [10, 20, 30, 40, 50]
value = 50

if Search(list, value):
    print("Found at Position", pos)
else:
    print("Not found")
