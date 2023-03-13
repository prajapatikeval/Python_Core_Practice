num = 1
if num == 1:
    print("Prime")

for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
