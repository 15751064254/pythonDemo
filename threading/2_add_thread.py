import threading

def thread_job():
  print('This is an added Thread, number is %s' % threading.current_thread())


def main():
  thread = threading.Thread(target = thread_job) #定义线程
  thread.start() #让线程开始工作

#  print('active_count():', threading.active_count())
#  print('enumerate():', threading.enumerate())
#  print('current_thread():', threading.current_thread())


if __name__ == '__main__':
  main()
