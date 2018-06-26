#ques 1:

import threading
from threading import Thread
import time
import math

class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(5)
        print("1st question value after 5 sec is",self.h)

thread1 = mythread(1)
thread1.start()

#ques 2:


class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print("value is",self.h)

for i in range(10):
    time.sleep(1)
    threadi=mythread(i)
    threadi.start()

#ques 3:

list=[15,12,17,159,55]
t=[2,4,6,8,10]
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        print("Done***")

for i,j in zip(list,t):
    time.sleep(j)
    print(j)
    print(i)


thread4=mythread()
thread4.start()

#ques 4:

class mythread(threading.Thread):
    def __init__(self,fact):
        threading.Thread.__init__(self)
        self.h=fact

    def run(self):
        print("factorial of "+str(self.h)+" is "+str(math.factorial(self.h)) )

fact=int(input("Enter the number for factorial"))
thread5=mythread(fact)
thread5.start()