#文件读写

#读文件
f = open(r'd:\py\day1.py','r')
#print(f)
#print(f.readlines())
#print(f.close())
# try:
#     f = open(r'd:\py\day1.py', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#with open(r'd:\py\day1.py','r') as f:#with语句自动调用close()方法
    #print(f.read())
#read():会一次性读取文件的全部内容
#read(size):每次最多读取size个字节的内容
#readline():可以每次读取一行内容
#readlines():一次读取所有内容并按行返回list
# for line in f.readlines():
#     print(line.strip()) # 把末尾的'\n'删掉


f = open(r'e:\a1.mp4','rb')#读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
#print(f.read())
#print(f.close())

f = open(r'e:\a1.mp4','r',encoding='gbk')#读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#print(f.read())

f = open(r'e:\a1.mp4','r',encoding='gbk',errors = 'ignore')#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
#print(f.read())
#print(f.close())

#写文件:与读文件一样只是把r改成w就行
# with open('', 'w') as f:
#     f.write('Hello, world!')

import os
a = os.listdir('d:\py')
#print(a)
for w in a:
    #print('d:\py\\'+w)
    path = 'd:\py\\'+w
    if path.endswith(".py"):
        #print(path)
        pass
    print(path)
with open('path.py','a') as f:
    f.write('Hello world')
    f.close()