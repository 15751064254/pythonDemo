import threading
from queue import Queue
import copy
import time

def job(l, q):
  res = sum(l)
  q.put(res)

def multithreading(l):
  q = Queue()
  threads = []
  total = 0

  for i in range(4):
    t = threading.Thread(target = job, args = (copy.copy(l), q), name = 'T%i' % i)
    t.start()
    threads.append(t)

  [t.join() for t in threads]

  for _ in range(4):
    total += q.get()

  print(total)


def normal(l):
  total = sum(l)
  print(total)
    

if __name__ == '__main__':
  l = list(range(1000000))
  st = time.time()
  normal(l*4)
  t = time.time()
  print('normal:', t - st)

  st = time.time()
  multithreading(l)
  t = time.time()
  print('multithreading:', t - st)
