#高阶函数
f = abs#变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同,变量可以指向函数.
#print(f(-10))
def add(x, y, f):
    return f(x) + f(y)

#print(add(-5, 6, abs))
#map()函数
k=list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#print(k)

#reduce()函数
#对一个序列求和
from functools import reduce
def add(x, y):
    return x + y
#print(reduce(add, [1, 3, 5, 7, 9]))

#filter()函数用于过滤序列。
def is_odd(n):
    return n % 2 == 1
b=list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
#print(b)

#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
n=list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
#print(n)

#sorted()函数
m=sorted([36, 5, -12, 9, -21])
#print(m)从小到大排序
b=sorted([36, 5, -12, 9, -21], key=abs)#按绝对值大小排序
#print(b)
c=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)#实现忽略大小写的排序
#print(c)
v=sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)#进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
#print(v)


#返回函数,函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
#print(f())#调用lazy_sum()时，返回的并不是求和结果，而是求和函数，调用函数f时，才真正计算求和的结果
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)#f1和f2是两个不同的函数

#nonlocal
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn
k = int()
f = inc()
print(f())
from inspect import isfunction
#if(hasattr(f,'__call__')):
    #print(1)
#else:
    #print(2)
if(isfunction(k)):
    print(1)
else:
    print(2)
