#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
import os
from multiprocessing import Process

def run_fork(name):
    print('run child process %s (child id %s parent id %s)' % (name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('parent id %s' % os.getpid())
    p = Process(target=run_fork, args=('testhaha', ))
    print('child will start......')
    p.start()
    p.join()
    print('child process end  parent id %s' % os.getpid())
'''


print('haha')

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('write process %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s into Queue' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('read process %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from Queue' % value)

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
