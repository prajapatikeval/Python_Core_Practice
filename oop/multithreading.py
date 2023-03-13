from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)  # it will sleep for 1 second


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()
# in thread class we have method run if you change the method name it will not work that why we are using start
t1.start()
sleep(0.2)
t2.start()
'''it will create total of three thread one is main and two is t1 and t2'''

t1.join()
t2.join()  # main thread will wait to complete a execution of t1 and t2 thread after that it will print
# bellow codes

print("Bye")
