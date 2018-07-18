# -*- coding: utf-8 -*-

import multiprocessing
import threading
import time
import os

# print os.getpid()
class Test(object):
    def __init__(self, val=None):
        self.val = val
    @classmethod
    def add(cls, a, b):
        print a+b

class Exam(object):
    def __init__(self, score):
        self.__score = score
    @staticmethod
    def pr():
        print "this is staticmothod"
    @staticmethod
    def add(a, b):
        print a+b

Test.add(2, 3)
Exam.pr()
Exam.add(1, 2)
'''
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
'''
'''
def loop(list=[1,2,3]):
    print "thread %s is running..."%threading.current_thread().name
    for i in list:
        print "thread %s >>> %s" %(threading.current_thread().name, str(i))
        time.sleep(1)
    print "thread %s is ended" %threading.current_thread().name

print "thread %s is running ..." %threading.current_thread().name
list1 = [0,1,2,3,4,5,6,7,8]
list2 = ["a", "b", "c", 11, 12, 13, 14, 15, 16]
t1 = threading.Thread(target=loop, args=(list1, ), name="Tread_t1")
t2 = threading.Thread(target=loop, args=(list2, ), name="Tread_t2")
t1.start()
t2.start()
t1.join()
t2.join()
print "tread %s ended " %threading.current_thread().name
'''