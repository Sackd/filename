#错误处理
#try
#try:
#     print('try...')
#     r = 10 / 2
#     print('result:', r)
# except ZeroDivisionError as e:#若前面出错，则执行except语句块：没出错，就不会执行
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:#值错误
#     print('ValueError:', e)
# except ZeroDivisionError as e:#零除错误
#     print('ZeroDivisionError:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:#没有错误发生时，会自动执行else语句：
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# try:#第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')#统一码错误

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:#如果调用的其他函数出错，也可以捕获错误
#         print('Error:', e)
#     finally:
#         print('finally...')
# print(main())

#调用栈
# err.py:
# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     bar('0')

# print(main())


#记录错误: logging模块(程序打印完错误信息后会继续执行，并正常退出：)

# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# main()
# print('END')


#抛出错误
# err_raise.py
# class FooError(ValueError):
#     pass

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n

# foo('0')
# s = FooError()
# print(s.foo())

# err_reraise.py

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise

# bar()

try:
    10 / 0
except ZeroDivisionError:#在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
    raise ValueError('input error!')
