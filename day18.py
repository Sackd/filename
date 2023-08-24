#调试
# def foo(s):#第一种方法就是用print()把可能有问题的变量打印出来看看
#     n = int(s)
#     #print('>>> n = %d' % n)
#     return 10 / n

# def main():
#     foo('0')

# #print(main())


# #第二种方法断言(assert):可以用-O(大写)参数来关闭assert：
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'#assert的意思是，表达式n != 0应该是True
#     return 10 / n

# def main():
#     foo('0')
# #print(main())


# #第三种方法logging：可以输出到文件。
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# #print(10 / n)


#第四种方法pdb(以参数-m pdb启动):让程序以单步方式运行，可以随时查看运行状态
s = '0'
n = int(s)
print(10 / n)

#第五种方法pdb.set_trace()：在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
#print(10 / n)



