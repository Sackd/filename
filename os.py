import os,sys
path = 'd:\py'
def rename(path):
    for file in os.listdir(path):#对目录下的文件进行遍历

        if file.startswith("day") and file.endswith(".py"):#判断是否是文件
            print(file)
            newName = file.replace("day00","day")#设置新文件名
            os.rename(os.path.join(path,file),os.path.join(path,newName))#重命名
rename(path)
print("End")


# import os

# def re_fileName(path):
#     fileList = os.listdir(path)
#     num = 1
#     for file in fileList:
#         used_fileName,extension = os.path.splitext(file)
#         new_file = str(num)+extension:
#         os.rename(file,new_file)
#         print("文件%s的新文件名为:%s"%(path+file,path+new_file))
#         num +=1
# if __name__=='__main__':
#     path = os.getcwd()
#     re_fileName(path)