#使用枚举类
from enum import Enum#获得了Month类型的枚举类

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#print(Month.Jan)
#for name, member in Month.__members__.items():
#    print(name, '=>', member, ',', member.value)#value属性则是自动赋给成员的int常量，默认从1开始计数。

from enum import Enum, unique#从Enum派生出自定义类
@unique#可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon
#print(day1)#访问这些枚举类型可以有若干种方法
# print(Weekday.Tue)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(day1 == Weekday.Mon)
# print(day1 == Weekday.Tue)
# print(Weekday(1))
# print(day1 == Weekday(1))
#for name, member in Weekday.__members__.items():
    #print(name, '=>', member)

#type():既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
# print(h.hello())
#print(type(Hello))
#print(type(h))
#metaclass(元类):控制类的创建行为

a = range(2)
for i in range(2):
    print(i)