#查看目标目录下所有文件
import os
path = os.curdir
for root,folders,files in os.walk(path):
    for file in files:
        print(file)
