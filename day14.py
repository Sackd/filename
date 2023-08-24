#多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):#定义好runnable和flyable的类
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
class Dog(Mammal, Runnable):#给Dog类加上Runnable的功能
    pass
class Bat(Mammal, Flyable):#给Bat类加上flyable的功能
    pass
#MixIn:同时继承两个类的设计（目的是给一个类增加多个功能
#class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
#class MyTCPServer(TCPServer, ForkingMixIn):#多进程模式的TCP服务
    pass
#class MyUDPServer(UDPServer, ThreadingMixIn):#多线程模式的UDP服务
    pass     
#class MyTCPServer(TCPServer, CoroutineMixIn):#更先进的协程模型
    pass