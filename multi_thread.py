import threading
import time
import concurrent.futures

# How to use class
def main_class():
    t1 = TestThread()
    t1.setDaemon(True)
    t1.start()
    t1.join()
    print("end")

# How to use instance
def main_instance():
    t1 = threading.Thread(target=foo, name="foo", args=(5,))
    t1.setDaemon(True)
    t1.start()
    t1.join()
    print("end")

# How to use Threadpool
def main_threadpool():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(func1)
    executor.submit(func2)

class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        for i in range(5):
            time.sleep(1)
            print("sub thread : " + str(i))

def foo(n):
    for i in range(n):
        print("sub thread : " + str(i))

def func1():
    while True:
        print("func1")
        time.sleep(1)


def func2():
    while True:
        print("func2")
        time.sleep(1)

if __name__ == '__main__':
    main_class()
    #main_instance()
    #main_threadpool()
