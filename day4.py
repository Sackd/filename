#列表生成式

#L2 = [x if True==isinstance(x,str) else None for x in L1]
#print(x)



#生成器
#创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#g=(x * x for x in range(10))
#print(next(g))
#print(next(g))
#for n in g:
   #print(n)
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#print(fib(100))
def odd():
    print('step 1')
    yield 1#yield是返回值
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()#其中"o = odd"就是生成器对象
#print(next(o))


#迭代器  Iterator
#使用isinstance()判断一个对象是否是Iterable(可迭代)对象：
from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance(100, Iterable))
#使用isinstance()判断一个对象是否是Iterator对象
from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
a=isinstance(iter([]), Iterator)
print(a)