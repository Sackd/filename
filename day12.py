#使用__slots__
class Student(object):#定义Student类
    pass
s = Student()#类化实例
s.name = 'Michael'#给实例绑定一个属性
#print(s.name)#打印实例属性
def set_age(self,age):#定义一个函数作为实例方法
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)#调用实例方法
#print(s.age)
s2 = Student()#创建新的实例
#print(s2.set_age(25))#尝试调用方法
def set_score(self,score):
    self.score = score
Student.set_score = set_score#给class绑定方法，类方法
s.set_score(100)
#print(s.score)#给class绑定方法后，所有实例均可调用：
s2.set_score(99)
#print(s2.score)
class Student(object):
    __slots__ = ('name','age')#用tuple定义允许绑定的属性名称,其中的’ __slots__‘仅对类实例起作用；除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
s = Student()#创建新实例
s.name = 'Michael'#绑定属性‘name'
s.age = 25#绑定属性'age'
#s.score = 99#绑定属性'score'

