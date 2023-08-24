#分布式进程：把多个进程分布到多个机器上
#  master.py

import random,time,queue #导入随机，时间，队列模块
from multiprocessing.managers import BaseManager #导入多进程管理
from multiprocessing import freeze_support #网上看到的不知道干什么用，只知道是win10防出错

task_queue = queue.Queue()  #实例化队列为任务队列
result_queue = queue.Queue()  #实例化队列为结果队列

def return_task_queue():  #win下queuemanager注册到网络关联队列不能用lambda，所以自定义一个函数用于关联
    global task_queue
    return task_queue

def return_result_queue():  #win下queuemanager注册到网络关联队列不能用lambda，所以自定义一个函数用于关联
    global result_queue
    return result_queue

class QueueManager(BaseManager): #定义QueueManager继承BaseManager
    pass

def test():
    QueueManager.register('get_task_queue',callable=return_task_queue)   #注册任务队列到网络
    QueueManager.register('get_result_queue',callable=return_result_queue)   #注册结果队列到网络

    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')   #创建QueueManager实例，绑定ip、验证码

    manager.start()   #打开服务器

    task = manager.get_task_queue()   #通过QueueManager获取任务队列，避免绕过封装
    result = manager.get_result_queue() #同上

    for i in range(10):
        n = random.randint(0,10000)  #生成任务数字（随机数）
        print('Put task %d...' % n)  
        task.put(n)                  #将任务数添加到任务队列

    print('Try get result...')

    try:
        for i in range(10):          
            r = result.get(timeout=10)  #监听结果队列，获取结果数
            print('Result:%s' % r)
    except queue.Empty:
        print('queue is empty')         #调试空队列错误
    finally:
        manager.shutdown()              #不管前面代码是否有误，只要manager.start()，必须关闭，不然再次打开会报错
        print('master exit.')


if __name__ == '__main__':
    freeze_support()
    print('Start!')
    test()

# import time,sys,queue
# from multiprocessing.managers import BaseManager

# class QueueManager(BaseManager):  #定义QueueManager类，继承BaseManager
#     pass

# QueueManager.register('get_task_queue')   #worker无需生成队列，直接注册
# QueueManager.register('get_result_queue')

# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)  #输入服务器ip

# m = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')  #创建QueueManager实例，绑定ip、验证码

# m.connect()   #连接服务器

# task = m.get_task_queue()     #通过QueueManager获取任务队列，避免绕过封装
# result = m.get_result_queue()

# for i in range(10):
#     try:
#         n = task.get(timeout=1)  #从任务队列中获取任务数
#         print('run task %d * %d...' % (n,n))
#         r = '%d * %d = %d' % (n,n,n*n)  #worker完成计算，得到结果数
#         time.sleep(1)
#         result.put(r)           #将结果数添加到结果队列
#     except queue.Empty:
#         print('task queue is empty')

# print('worker exit')

