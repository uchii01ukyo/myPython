# coding: UTF-8
import threading
import time
import concurrent.futures
import multiprocessing

# How to use class
def main_class():
    t1 = TestThread()
    t1.setDaemon(True)
    t1.start()
    t1.join()
    print("end")

class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("sub thread : " + str(i))

# How to use instance
def main_instance():
    t1 = threading.Thread(target=foo, name="foo", args=(5,))
    t1.setDaemon(True)
    t1.start()
    t1.join()
    print("end")

def foo(n):
    for i in range(n):
        print("sub thread : " + str(i))

# How to use Threadpool
def main_threadpool():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(func1)
    executor.submit(func2)

def func1():
    while True:
        print("func1")
        time.sleep(1)

def func2():
    while True:
        print("func2")
        time.sleep(1)


# How to use multiprocess
def main_multiprocess():
    p = multiprocessing.Process(target=func_2, args=(10,))
    p.start()
    func_1(10)

def func_1(num):
    print('main_Start')
    for i in range(num):
        print('main_process:'+ str(i))
        time.sleep(1)
    print('main_End')

def func_2(num):
    print('sub_Start')
    for i in range(num):
        print('sub_process:' + str(i))
        time.sleep(0.5)
    print('sub_End')


if __name__ == '__main__':
    #main_class()
    #main_instance()
    #main_threadpool()
    main_multiprocess()
