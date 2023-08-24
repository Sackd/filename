#序列化(picking)
#d = dict(name='Bob',age=20,score=88)#定义一个dict

#把一个对象序列化并写入文件
import pickle
d = dict(name='Bob',age=20,score=88)
#print(pickle.dumps(d))#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件


#pickle.dump()直接把对象序列化后写入一个file-like
# f = open('dump.txt','wb')
# pickle.dump(d,f)
# print(f.close())

#反序列化
#用pickle.load()方法从一个file-like Object中直接反序列化出对象
# f = open('dump.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)



#JSON:在不同的编程语言之间传递对象，就必须把对象序列化为标准格式
import json
d = dict(name='Bob',age=20,score=88)
#print(json.dumps(d))#dumps()方法返回一个str，内容就是标准的JSON
json_str = '{"age":20,"score":88,"name":"Bob"}'
#print(json.loads(json_str))#loads():把JSON的字符串反序列化


#JSON进阶
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob',20,88)
#print(json.dumps(s))

def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
#print(json.dumps(s,default=student2dict))#Student实例首先被student2dict()#函数转换成dict，然后再被顺利序列化为JSON：
#print(json.dumps(s,default=lambda obj: obj.__dict__))#任意class的实例变为dict：


#JSON反序列化为类的对象实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))#打印出的是反序列化的Student实例对象