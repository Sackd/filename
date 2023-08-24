#实现index方法
class Listindex(object):
    def __init__(self,list1 = []):#调用一个列表属性，在类化实例时init自动被调用，那么list属性属于实例属性。但list1这个属性在下面的方法中名字都是相同的
        self.list1 = list1
    def index(self,value):
        list2 = []
        dic = {}
        z = -1
        for i in self.list1:
            z = z + 1 
            
            if i  not in list2:
                list2.append(i)
                dic[i]=z
            else:
                list2.append(i)
        return dic[value]
s = Listindex(list1=['a','s','q','h','a','w','w','c','g','g'])
print(s.index('w'))
    