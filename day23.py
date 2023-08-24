#操作文件和目录
# import os#os模块的基本功能
# print(os.name)
# print(os.environ)#环境变量：在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# print(os.environ.get('PATH'))#获取某个环境变量的值


# print(os.path.abspath('.'))#查看当前目录的绝对路径
# print(os.path.join('d:\py','0.py'))#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.mkdir('d:\py\0.py'))#创建一个目录
# print(os.rmdir('d:\py\0.py'))#删除一个目录
# print(os.path.split('d:\py\0.py'))#拆分路径
# print(os.path.splitext('d:\py\0.py'))#得到文件扩展名
# print(os.rename('test.txt', 'test.py'))#文件重命名
# print(os.remove('test.py'))#删除文件
# print([x for x in os.listdir('.') if os.path.isdir(x)])#列出当前目录下的所有目录，只需要一行代码：
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])#列出所有的.py文件
