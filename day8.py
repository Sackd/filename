' a test module '

__author__ = 'Michael Liao'

import sys#就是导入该sys模块

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
    
#作用域
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):#公开的reeting()函数：外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
print(greeting('mad'))



#安装第三方模块
import sys
sys.path.append('/Users/michael/my_py_scripts')
print(sys)
