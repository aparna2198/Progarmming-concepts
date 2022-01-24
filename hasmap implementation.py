# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 20:47:51 2022

@author: APARNA
"""
#  first it allocates list in ram 
# hash functions maps key to a specific element in the list and index of that element is given by hash function 
# hash function converts string into an index into an array  

# using ascii number
# def get_hash(key):
#     h = 0
#     for char in key:
#         h+=ord(char)
#     return h%1000

# simple implementations 
class Hashtable:
    
    def __init__(self):
        self.max =  10
        self.arr = [None for i in range(self.max)]
    
    def get_hash(self,key):
        
        h = 0
        for c in key:
            h+=ord(c)
        print(h%self.max)
        return h%self.max
    
    def __getitem__(self,key):
        hashval = self.get_hash(key)
        return self.arr[hashval]
    
    def __setitem__(self,key,val):
        hashval = self.get_hash(key)
        self.arr[hashval] = val

ob  = Hashtable()

ob['a'] = 1
ob['b'] = 2

print(ob.arr)

print(ob['c'])

# collision problem
# ob = Hashtable()

# ob['march 6'] = 100
# ob['march 17'] = 101

# print(ob['march 6'])
# print(ob['march 17'])

        
    