#匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#匿名函数lambda x: x * x实际上就是
def f(x):
    return x * x
f = lambda x: x * x
print(f(5))
#装饰器:在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式叫装饰器
#函数对象有一个__name__属性，可以拿到函数的名字：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def now():
    print('2015-3-25')
f = now
#print(f)
n=now.__name__
print(n)
m=f.__name__
print(m)

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log#这行和下一行相当于执行了语句now = log(now)
def now():
    print('2015-3-25')
print(now())