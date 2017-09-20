import threading
import time
from queue import Queue

def job(l, q):
  for i in range(len(l)):
    l[i] = l[i] ** 2
  q.put(l)


def multithreading():
  data = [[1, 2, 3], [3, 4, 5], [4, 4, 4],[5, 5, 5]]
  q = Queue()
  threads = []
  results = []

  for i in range(len(data)):
    t = threading.Thread(target = job, args = (data[i], q))
    t.start()
    threads.append(t)

  for thread in threads:
    thread.join()

  for _ in range(len(data)):
    results.append(q.get())

  print(results)

if __name__ == '__main__':
  multithreading()
