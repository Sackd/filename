#StringIO和BytesIO
#StringIO:在内存中读写str
from io import StringIO
f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.write('world!'))
# print(f.getvalue())#getvalue()方法用于获得写入后的str


# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#        break
#     print(s.strip())


#BytesIO:在内存中读写bytes
# from io import BytesIO
# f = BytesIO()
# print(f.write('中文'.encode('utf-8')))#写入的不是str，而是经过UTF-8编码的bytes。
# print(f.getvalue())
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
