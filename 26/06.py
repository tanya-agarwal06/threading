'''import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        print("value send",self.h)
thread1 = mythread(1)
thread1.start()
time.sleep(5)
thread2 = mythread(2)
thread2.start()


#threading
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        time.sleep(1)
        print("no is",self.h)

for i in range(10):
    thread1=mythread(i)
    thread1.start()
print("active threads are",threading.activeCount())


#join in threading
import threading
from threading import Thread
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("hello i am in run",self.h)
thread1 =mythread("from mythread 1")
thread1.start()
thread1.join()
thread2= mythread("from mythread 2")
thread2.start()
thread2.join()
print("good girl")'''


#deadlock situation
def sleep(i):
    print("thread %s going to sleep in 5 seconds")
    
