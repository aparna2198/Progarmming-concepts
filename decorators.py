# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:05:07 2021

@author: APARNA
"""

# =============================================================================
# 
# decorators is a function which 
# takes another function as an argument adds some kind of functionality 
# and return another function 
#all of this without altering the source code of the original function that we pass in
# execute function that is passed in ->decorators job   
# =============================================================================


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

    



        
        
        
        