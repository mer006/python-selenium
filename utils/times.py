#! usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import datetime
from functools import wraps

def timestamp():
    '''时间戳'''
    return time.time()

def dt_strftime(fmt='%Y%m%d'):
    '''
    datetime格式化时间
    :param fmt "%Y%m%d %H:%M:%S"
    '''
    return datetime.datetime.now().strftime(fmt)

def sleep(seconds=1):
    #睡眠时间，默认1s
    time.sleep(seconds)

def running_time(func):
    '''函数运行时间'''
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = timestamp()
        res = func(*args,**kwargs)
        print("函数运行结束，用时%.3f"%(timestamp()-start))
        return res
    return wrapper