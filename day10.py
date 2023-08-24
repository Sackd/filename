#继承和多态
class Animal(object):#定义类名为Animal,继承类是object

    def run(self):#定义一个run方法直接打印

        print('Animal is running...')
x = Animal()#实例化类
#print(x.run())#调用类中的方法格式：类名.方法名
              #调用类中的属性（变量）：类名.属性

class Dog(Animal):#子类是Dog
    pass

class Cat(Animal):#子类是Cat
    pass
dog = Dog()
#print(dog.run())
cat = Cat()
#print(cat.run())
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):#给子类增加一些方法
        print('Eating meat...')
c = Dog()
#print(c.run())
#print(c.eat())
class Dog(Animal):
    def run(self):
        print('Dog is running...')
d = Dog()
#print(d.run())
class Cat(Animal):
    def run(self):
        print('Cat is running...')
c = Cat()
f = Animal()
#print(f.run())
a = list()
#print(isinstance(a,list))#判断一个变量是否是某个类型可以用isinstance()判断：
c = Dog()
#print(isinstance(c,Animal))#c不仅仅是Dog，c还是Animal！
b = Animal()
#print(isinstance(b, Dog))#Dog可以看成Animal，但Animal不可以看成Dog。

def run_twice(animal):
    animal.run()
    animal.run()
#print(run_twice(Animal()))#传入Animal实例
#print(run_twice(Dog()))#传入Dog实例
class  Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
print(run_twice(Tortoise()))



#获取对象信息
print(type('adg'))#基本类型都可以用type()判断：