# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 01:21:12 2022

@author: APARNA
"""


# A few good examples are when you want to add logging, 
# test performance, perform caching, verify permissions,

import time
events = []
def timeit(func):
    
    def wrapper():
        global events
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print(f"time take by {func.__name__} is {t2-t1}")
        events.append(f"function {func.__name__} executed")
    return wrapper

@timeit
def do_something():
    time.sleep(1)
    
ob = do_something()

# dob = timeit(do_something)()

    



        
        
        
        