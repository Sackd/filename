#偏函数
int('453')#int()函数可以把字符串转换为整数
#print(int('453'))
#传入base参数，就可以做N进制的转换
a=int('12345',base=8)#八进制
#print(a)
q=int('12345',16)
#print(q)
#转换大量的二进制字符串,可以定义一个int2()的函数，默认把base=2传进去：
def int2(x,base=2):
    return int(x,base)
#print(int2('1000000'))
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))
print(int2('1000000',base=10))#可以在函数调用时传入其他值：
