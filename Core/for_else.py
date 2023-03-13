nums = [11, 16, 18, 21, 26]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
    else:
        print("Not found")
# In this method if number is divided by 5 is not found in list than it will print else condition as len(list)

print(5*"-", "Second method", 5*"-")
'''so unless that we use this method but break is mandatory'''
for num in nums:
    if num % 5 == 0:
        print(num)
else:
    print("not found")
