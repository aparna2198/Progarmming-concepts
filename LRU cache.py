# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 01:48:12 2022

@author: APARNA
"""
from collections import OrderedDict
import time
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        self.max = cap
        self.arr = OrderedDict()
       
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        
        if self.arr.get(key,None) is not None:
            self.arr.move_to_end(key)
            return self.arr[key]
        else:
            return -1
    #Function for storing key-value pair.   
    def set(self, key, value):
        if self.arr.get(key,None) is not None:
            self.arr.move_to_end(key)
        self.arr[key] = value
        
        if len(self.arr)>self.max:
            self.arr.popitem(last = False)

cache = LRUCache(4)





t1 = time.perf_counter()
# sample to bulk test
with open('fileinput.txt','r') as f:
    lines = f.readlines()

for i in lines:
    try:
        
        
        
        a= i.split(' ')[0]
        if a == 'SET':
            parts = i.split(' ')
            cache.set(int(parts[1]),int(parts[2]))
        elif a == 'GET':
            parts = i.split(' ')
            
        if  a == 'GET' and int(parts[1])==30:
            break
        #     print("arr",cache.arr)
        #     print("his",cache.history)
    except Exception as e:
        print(str(e))
        print("arr",cache.arr)
t2 = time.perf_counter()
    
print("diff",t2-t1)
        
        











                