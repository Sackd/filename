import time
start_time = time.time()
from multiprocessing import Pool


def js(arg):
    for item in range(200000000):
       arg += item
for i in range(3):
    js(i)
    pass

end_time = time.time()

# Running time:17.165452003479004 秒
print('Running time:%s 秒'%(end_time-start_time))

# Running time:5.931505918502808 秒
# if __name__=='__main__':
#   start_time = time.time()
#   p = Pool(3)
#   for i in range(3):
#       p.apply_async(js, args=(i,))
#       pass
#   p.close()
#   p.join()
#   end_time = time.time()
#   print('Running time:%s 秒'%(end_time-start_time))
#   pass