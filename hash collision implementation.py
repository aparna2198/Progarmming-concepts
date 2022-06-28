# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:44:28 2022

@author: APARNA
"""
# this is just to play with git commits 
# chaining to resolve collision
class HashTable:
    
    def __init__(self):
        self.max= 10
        self.arr = [[] for i in range(self.max)]
        
    def gethash(self,key):
        h = 0
        for c in key:
            h+=ord(c)
        # print(h%self.max)
        return h%self.max

    def __setitem__(self,key,val):
        hashval = self.gethash(key)
        for idx, ele in enumerate(self.arr[hashval]):
            if ele[0] == key:
                self.arr[hashval][idx] = (key,val)
            
        self.arr[hashval].append((key,val))
        
    def __getitem__(self,key):
        hashval = self.gethash(key)
        for idx, ele in enumerate(self.arr[hashval]):
            if ele[0] == key:
                return self.arr[hashval][idx][1]
        
    def __delitem__(self,key):
        hashval = self.gethash(key)
        for idx, ele in enumerate(self.arr[hashval]):
            if ele[0] == key:
                self.arr[hashval][idx] = []
        
                
ob = HashTable()

ob['march 6'] = 100
ob['march 17'] = 101

print(ob['march 6'])
print(ob['march 17'])

del ob['march 17']
print(ob['march 17'])

del ob['march 9']
print(ob['march 17'])




                
                