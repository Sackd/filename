class Student(object):#定义类
    pass
#bart = Student()#创建实例:类名加（）
#print(bart)
#print(Student)
#bart.name = 'Bart Simpson'#给实例bart绑定一个name属性
#print(bart.name)
    def __init__(self,name,score):#self指的就是bart这个实例本身
        self.name = name
        self.score = score
bart = Student('Bart Simpson',59)
def print_score(std):
    print('%s: %s' % (std.name, std.score))
#print(print_score(bart))


#获取对象信息
#print(type('adg'))#基本类型都可以用type()判断：
#print(type(abs))#如果一个变量指向函数或者类，也可以用type()判断：
#print(type(Student))
#print(type(123)==type(456))#如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
#print(type('abc')==str)

import types
def fn():
    pass

#print(type(fn)==types.FunctionType)

#print(type(abs)==types.BuiltinFunctionType)

#print(type(lambda x: x)==types.LambdaType)

#print(type((x for x in range(10)))==types.GeneratorType)
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
b = Animal()
d = Dog()
h = Husky()
#print(isinstance(h,Husky))#判断class的类型，可以使用isinstance()函数
#print(isinstance(h,Dog))
#print(isinstance([1, 2, 3], (list, tuple)))#并且还可以判断一个变量是否是某些类型中的一种
#print(dir('ABC'))#获得一个对象的所有属性和方法，可以使用dir()函数
#print(len('ABC'))
#print('ABC'.__len__())
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
#print(len(dog))
#print(dog.__len__())
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
#print(hasattr(obj, 'x'))#有属性x吗
#print(hasattr(obj,'y'))#有属性y吗
#setattr(obj, 'y', 19)#设置一个属性y
#print(hasattr(obj,'y'))#现在有了属性y
#print(getattr(obj, 'y'))#获取属性y
#print(obj.y)#获取属性y
#print(getattr(obj,'z'))
#print(getattr(obj,'z',404))#可以传入一个default参数，如果属性不存在，就返回默认值
#print(hasattr(obj, 'power'))#有属性power吗
#print(dir(obj))
#print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
#print(fn())



#实例属性和类属性
class Student(object):
    def __init__(self,name):
        self.name = name
s = Student('Bob')
s.score = 90
#print(s.score)
class Student(object):
    name = 'Student'
s = Student()#创建实例
#print(s.name)#打印name属性，因为实例没有name属性，所以会继续查找class的类属性
#print(Student.name)#打印类的name属性
s.name = 'Michael'#给实例绑定name属性
#print(s.name)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
#print(Student.name)#但是类属性并未消失，用Student.name仍然可以访问
del s.name#删除实例的name属性
print(s.name)# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
