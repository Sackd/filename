
import time,psutil,os,sys,re,unittest
# sys

#import re
#print('arguments are:')
# for i in sys.argv:
#     print i
# print(argv[1])
# import pdb
# pdb.set_trace()
start_time = time.time()
#print(len(sys.argv))


    #import psutil
#import os
#p = sys.argv[1]
#re.search(pattern=r'^-\w\w$r',string=sys.argv[1])
list1 = []
dic = {}
dic1 = {}
dic2 = []
#all_dirs = []

def main(r,h):
    try:

        files = os.listdir(r)#os.listdir函数:返回指定文件夹下的文件名字的列表
        # for root,dirs,list1 in os.walk(rootPath):
        #     for 
        #         if dirs != []:
        #             all_dirs.append(dirs)
        #             #dirs.remove(dirs)
        #             print(all_dirs[-1])
        for file in files:
            q = r + '/' + file
            # for root,dirs,list1 in os.walk(rootPath):
            #     print(root,dirs,list1)
            if os.path.isdir(q):#os.path.isdir函数：判断是否为目录
                main(q,h)
                #print(file)
                
            else:
                #build_time = time.ctime(os.path.getctime(q))
                
                
                canshu = re.match(r'^(?=.*[0-9])(?=.*[a-zA-Z])(.{0,1000})$',h) 
                
                if canshu:
                    
                
                #list1.append(q)
                #file_size = os.path.getsize(q)
                #dic[q] = file_size
                #sorted(file_size)
            #if re.match(r'\w{10}',sys.argv[4]):
                    if canshu.group() in file:
                        list1.append(file)
                #print('in is in',file) 
                        file_size = os.path.getsize(q)
                        dic[q] = file_size
                        t = os.path.getmtime(q)
                        timeStruce = time.localtime(t)
                        build_time = time.strftime('%Y-%m-%d %H:%M:%S',timeStruce)
                        dic1[q] = build_time
                        
                        #file_list = sorted(dic, key=lambda file:os.path.getctime(os.path.join(sys.argv[2],file)))
                else:
                    print('Error')
                    break
                 
    except OSError as e:
        print('//////',e)     
#main(sys.argv[2])     

def getdata(x,y,z):
    if x == 'size':
        file_size = sorted(y.items(),key=lambda x:x[1],reverse=False)
        for s in file_size:
            s=','.join(str(i) for i in s)
            #print(s)
            dic2.append(s)
    elif x == 'date':
        #build_time = time.ctime(os.path.getctime(main(sys.argv[2])))
        file_time = sorted(z.items(),key=lambda x:x[1],reverse=False)
        #file_time = sorted(dic, key=lambda file:os.path.getctime(os.path.join(sys.argv[2],file)))

    #print(len(file_list))
        for k in file_time:
            k = ','.join(str(i) for i in k)
            #print(k)
            dic2.append(k)
def receive(n,m,p):
    main(n,p)
    getdata( m, dic, dic1)
    return dic2
#print(receive(sys.argv[2],sys.argv[6],sys.argv[4]))


# m = 'a'
# for filewalks in os.walk("d:\\"[,topdown=True]):
#     for files in filewalks[2]:
#         if m in files:
#             print(m,'is in',os.path.join(filewalks[0],files))#打印存在in的文件
# class FileNamestTestCase(unittest.TestCase):

#     def test_file_name(self):
#         file_name = main(sys.argv[2])
#         self.assertEqual(file_name,'None')
# unittest.main()
# m = -1
# n = ''
# for x in dic:
#     if m < dic[x]:
#         n = x
#         m = dic[x]
#list2 = sorted(dic.items(),key=lambda x:x[1],reverse=False)#按内存大小排序
end_time = time.time()
#print(len(sys.argv))
#print(sys.argv)


#print('Running time:%s 秒'%(end_time-start_time))
#print(u'当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 ))
#Running time:5.411839246749878 秒
#当前进程的内存使用：18.4453 MB
#Running time:5.792630910873413 秒
#当前进程的内存使用：18.4531 MB
#Running time:5.664317846298218 秒
#当前进程的内存使用：18.3516 MB
#Running time:4.099440097808838 秒
#当前进程的内存使用：18.3750 MB