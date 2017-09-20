import threading
import time

def T1_job():
  print('T1 start \n')
  for i in range(10):
    time.sleep(0.1)
  print('T1 finish \n')


def T2_job():
  print('T2 start \n')
  print('T2 finish \n')


def main():
  thread_1 = threading.Thread(target = T1_job, name = 'T1')
  thread_1.start()

  thread_2 = threading.Thread(target = T2_job, name = 'T2')
  thread_2.start()

  thread_1.join()
  thread_2.join()

  print('all done \n')


if __name__ == '__main__':
  main()
