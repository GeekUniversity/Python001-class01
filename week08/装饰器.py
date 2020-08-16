# Author Andy Fang
# -*- coding:utf-8 -*-
import time
import  functools
def timer(func):
    @functools.wraps(func)
    def time_sum(*args, **kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print(f'function func total run time:{end_time - start_time}')
    return  time_sum
@timer
def func(*args, **kwargs):
    print('函数开始运行')
    time.sleep(2)
    print('函数运行结束')

func()