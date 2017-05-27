#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n<5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
'''
import threading, time

lock1 = threading.Lock() # 创建锁

def task2():
    lock1.acquire() # 获取锁
    try:
        for i in range(10):
            print('execute task2...')
    finally:
        lock1.release() # 释放锁

def task1():
    lock1.acquire() # 获取锁
    for i in range(10):
        print('execute task1...')
        time.sleep(5)
    lock1.release() # 释放锁

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()   
