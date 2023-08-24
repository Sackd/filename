#定制类
class Student(object):
    def __init__(self, name):
        self.name = name
#print(Student('Michael'))
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
#print(Student('Michael'))
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__
#print(Student('Michael'))
#__iter__
class Fib(object):#把一个类用于for in循环
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a#返回下一个值
#for n in Fib():
    #print(n)
#__getitem__ ： 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
#print(Fib()[5])
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
#print(f[1])
#print(list(range(100))[5:10])
#print(f[0:5])
class Fib(object):#使Fib拥有切片的功能
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
#print(f[0:5])
#print(f[:10:2])
#__getattr__
class Student(object):#当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':            
            return 99
s = Student()
#print(s.name)
#print(s.score)

class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
s = Student()
#print(s.age())
#print(s.abc)
#要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
#print(s.abc)
#__call__:直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
#print(s())
#callable()函数:我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))