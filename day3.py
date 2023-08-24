#计算x**2的函数
def power(x):
    return x*x
#print(power(5))


#x**n
def power(x,n):
    s = 1
    while n > 0:
        n=n-1
        s=s*x
    return s
#print(power(9,6))


#默认参数为2
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#print(power(6))


def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
#print(enroll('Sarah','F'))


def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
#print(enroll('Sarah','F'))





    