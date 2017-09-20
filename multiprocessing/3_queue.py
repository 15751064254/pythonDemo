import multiprocessing as mp

def job(q, a, b):
  res = a + b
  q.put(res)


if __name__ == '__main__':
  q = mp.Queue()
  p1 = mp.Process(target = job, args = (q, 1, 2))
  p1.start()
  p1.join()
  res = q.get()
  print(res)
