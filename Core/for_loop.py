x = ['a', 1, 'abc']
for i in x:
    print(i)

''''''

for i in [1, 2, 3, 4]:
    print(i)

''''''

for i in range(1, 10):
    print(i)
print()

'''Question'''
# Print perfect sqare number from 1 to 50


for i in range(1, 51):
    for j in range(1, 51):
        if i-j == 0:
            print(i**2)
