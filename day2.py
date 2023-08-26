def my_abs(x):
    if x >=0:
        return 1
    else:
        return 2


#list是可变的有序集合a
classmates = ['Michael', 'Bob', 'Tracy']
#print(classmates)
a=len(classmates)
#print(a)
#索引
print(classmates[0])
print(classmates[1])
print(classmates[-1])
#追加元素
classmates.append('Adam')
print(classmates)
#插入指定位置
classmates.insert(1, 'Jack')
print(classmates)
#删除末尾元素
classmates.pop()
print(classmates)
#删除指定位置元素
classmates.pop(1)
print(classmates)
#替换某元素
classmates[1] = 'Sarah'
print(classmates)
#二维数组下标0算第一个元素
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
#print(p[0])
#元组 不可变(指向不变)的有序集合
t = (1, 2)
print(t)
t = ()
print(t)

#条件判断if,if...else,elif(else if)

#循环 for...in 和 while
#for...in(把name带入到names中的每一个元素并一一列出来)
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
sum = 0
#(从1加到10)
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
#range() 生成0——4的整数序列
list(range(5))
print(list(range(5)))

#while 条件不满足退出循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#dict 和 set
#dict(key-value模式,key是不可变对象)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#通过in判断key是否存在：
print('Thomas' in d)
#通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas')
print(d.get('Thomas', -1))

#set(无序无重复)
s = set([1, 2, 3])
print(s)




classm = ['wu','shu']
print(classm)
print(len(classm))
classm.insert(0,'ma')
print(classm)
for name in classm:
    print(name)
sum = 0
for x in[1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)
print(list(range(100)))