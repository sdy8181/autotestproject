# -*- coding: UTF-8 -*-
import os
import threading
from time import ctime, sleep

def music(func):
    for i in range(10):
        print("I was listening to %s. %s" %(func, ctime()))
        sleep(1)

def move(func):
    for i in range(15):
        print("I was at the to %s. %s" % (func, ctime()))
        sleep(2)

threads = []
t1 = threading.Thread(target=music, args=('Alone',))
threads.append(t1)
t2 = threading.Thread(target=move, args=('Alone',))
threads.append(t2)

if __name__ == '__main__':
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()
    #
    # print('Done')
    path = "d:\\aaa"
    path1 = os.path.join(path, 'abc.log')
    print(path1)