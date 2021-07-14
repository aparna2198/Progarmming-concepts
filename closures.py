# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:28:18 2021

@author: APARNA
"""

# =============================================================================
# closure is an inner function that remembers and has access to variables in the local scope 
# in which it was created even after the outer function has finished executing.
# 
# -> closure closes over the free variables  from their envrionment - message free variable
# closures allow us to take advantage of first class functions 
# and return inner function that remembers
# and has access to variables local to the scope in which they were created
# =============================================================================

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func
    
hi_func = outer_func("hi")
hello_func = outer_func("hello")

hi_func()
hello_func()


        


