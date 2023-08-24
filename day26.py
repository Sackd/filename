#多线程
import time, threading
#current_thread():它永远返回当前线程的实例
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
# def loop():
#     print('thread %s is running...'% threading.current_thread().name)#主线程名字叫MainThread
#     n = 0
#     while n < 5:
#         n = n +1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')#子线程的名字在创建时自己指定
# t.start()#开始执行
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

#Lock:创建一个锁就是通过threading.Lock()来实现
# balance = 0
# lock = threading.Lock()

# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#            lock.release()

#多核cpu
# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
