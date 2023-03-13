
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [10, 20, 30, 33, 11, 7, 199]
even, odd = count(lst)
print("even : {} and odd : {}".format(even, odd))


# assignment
'''take 10 name from user and count and display number of user who has name length > 5'''


def name_count(lst):
    count = 0
    list = []
    for name in lst:
        if len(name) > 5:
            list.append(name)
            count += 1
    return count, list


# list = []
# for i in range(10):
#     name = input("enter a name")
#     list.append(name) from taking user we will use this


lst = ['rahul', 'sachin', 'elexender', 'vaishanavi',
       'durga', 'sam', 'dipika', 'akshat', 'bhargav', 'shiva']

count, list = name_count(lst)
print("Total name {} : {}".format(count, ", ".join(i for i in list)))
