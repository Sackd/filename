#类和实例
class Student(object):#定义类
    pass
bart = Student()#创建实例是类名+（）
#print(bart)
bart.name='Bart Simpson'#给一个实例变量绑定属性,给实例bart绑定一个name属性：
#print(bart.name)
class Student(object):

    def __init__(self, name, score):#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
        self.name = name#self指的就是实例本身
        self.score = score
bart = Student('Bart Simpson',59)
print(bart)
print(bart.name)
print(bart.score)
#数据封装
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):#类的方法
        print('%s: %s' % (self.name, self.score))

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):#给Student类增加新的方法，比如get_grade：
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
        print(get_grade('bob'))

#访问限制
class Student(object):

    def __init__(self, name, score):
        self.__name = name#实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__score = score#无法从外部访问

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

class Student(object):

    def get_name(self):#用该方法可以从外部访问
        return self.__name

    def get_score(self):
        return self.__score

class Student(object):

    def set_score(self, score):#用该方法允许外部代码修改score
        self.__score = score
#__xxx__：是特殊变量，特殊变量是可以直接访问的，不是private变量
#_name：这样的实例变量外部是可以访问的：但是，“虽然它可以被访问，但是，请把它视为私有变量，不要随意访问”
#
