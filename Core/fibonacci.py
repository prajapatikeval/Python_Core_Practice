def fib(n):
    a, b = 0, 1
    if n <= 0:
        print("Number should be greater than 0")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            sum = a+b
            a, b = b, sum
            print(sum)


fib(-2)


'''assignment'''
# we dont want to print all the fibonacci series number we just need the last number less than given value


def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Number should be greater than 0")
    elif n == 1:
        print(a)
    else:
        sum = 0
        for i in range(a, n):
            if sum + a <= n:
                sum = a+b
                a, b = b, sum
            else:
                break
        print("The last fibonacci number from the given number is : ", sum)


fib(100)
