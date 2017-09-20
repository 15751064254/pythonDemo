import multiprocessiong as mp
import threading as td

def job(a, b):
  print('aaaaa')


#t1 = td.Thread(target = job, args = (1, 2))
p1 = mp.Process(target = job, args = (1, 2))

#t1.start()
p1.start()

#t1.join()
#p1.join()
