def Sort(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j

        temp = list[i]
        list[i] = list[min]
        list[min] = temp
        print(list)


list = [5, -2**4, 3, 8, 6, 7, 2, 0, 10, -200]
Sort(list)
print(list)
