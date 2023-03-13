# in binary search it only work if list is sorted

pos = 0


def Search(list, value):
    lower = 0
    upper = len(list) - 1

    while lower <= upper:
        mid = (lower+upper)//2

        if list[mid] == value:
            globals()['pos'] = mid + 1
            return True
        else:
            if list[mid] < value:
                lower = mid + 1
            else:
                upper = mid - 1
    return False


list = [1, 2, 3, 4, 5]
value = 10

if Search(list, value):
    print("Found at position", pos)
else:
    print("Not found")
