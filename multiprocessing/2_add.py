import multiprocessing as mp

def job(q):
  print('job')
  res = 0
  for i in range(1000):
    res += i + i**2 + i**3
  q.put(res)


if __name__ == '__main__':
  q = mp.Queue()
  p1 = mp.Process(target = job, args = (q,))
  p1.start()
  p1.join()
  res1 = q.get()
  p2 = mp.Process(target = job, args = (q,))
  p2.start()
  p2.join()
  res2 = q.get()
  print(res1 + res2)
