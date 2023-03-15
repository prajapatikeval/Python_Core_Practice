name = ['a', 'b', 'c']
value = [1, 2, 3]

zipped = set(zip(name, value))
print(zipped)

# unzip
for name, val in zipped:
    print(name, val)
