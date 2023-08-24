class Screen(object):#练习
    @property
    def width(self):
        return self.width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self.height
    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width
s = Screen()
s.width = 1024
s.height = 768
int(s.resolution)
#print('resolution =',s.resolution)
#if s.resolution == 786432:
    #print('测试通过!')
#else:
    #print('测试失败!')



#使用@property
class Student(object):#定义

    def get_score(self):#这个方法用来设置成绩
         return self._score

    def set_score(self, value):#它用来获取成绩
        if not isinstance(value, int):#若成绩不是int----
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        else:
            self._score = value
s = Student()
s._score=60

print(s._score)
#print(s.set_score(9999))

class Student(object):

    @property#装饰器：把一个方法变成属性调用
    def score(self):#装饰器把一个getter方法变成属性
        return self._score

    @score.setter#@property本身又创建了另一个装饰器@score.setter
    def score(self, value):#把一个setter方法变成属性赋值
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score=60
print(s.score)


class Student(object):

    @property
    def birth(self):#bireth是可读写属性，既有setter，也有getter方法
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property#age是只读属性，只有getter方法，因为age可以根据birth和当前时间计算出来。
    def age(self):
        return 2015 - self._birth
s = Student()
s.birth = 2000
#print(s.age)