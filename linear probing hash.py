# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:06:15 2022

@author: APARNA
"""

# linear probing to resolve collision 

class HashTable:
    
    def __init__(self):
        self.max= 10
        self.arr = [None for i in range(self.max)]
        
    def gethash(self,key):
        h = 0
        for c in key:
            h+=ord(c)
        # print(h%self.max)
        return h%self.max

    def __setitem__(self,key,val):
        hashval = self.gethash(key)
        if self.arr[hashval] == None:
            self.arr[hashval] = (key,val)
        else:
            newhashval = self.find_slot(key,hashval)
            self.arr[newhashval] = (key,val)
    
    def get_prob_range(self,index):
        return [*range(index,len(self.arr))] + [*range(0,index)]
        
        
    def find_slot(self,key,index):
        prob_range = self.get_prob_range(index)
        for prob in prob_range:
            if self.arr[prob] is None:
                return prob
            if self.arr[prob][0] == key:
                return prob
                
    def __getitem__(self,key):
        hashval = self.gethash(key)
         
        prob_range = self.get_prob_range(hashval)
        for prob in prob_range:
            ele = self.arr[prob]
            if ele!= None and ele[0] == key:
                return ele[1]
        
        
    def __delitem__(self,key):
       
        hashval = self.gethash(key)
        prob_range = self.get_prob_range(hashval)
        
        for prob in prob_range:
            ele = self.arr[prob]
            
            if ele!= None and ele[0] == key:
                self.arr[prob]  = None
                
        
                
ob = HashTable()

ob['march 6'] = 100
ob['march 17'] = 101
ob.arr

print(ob['march 6'])
print(ob['march 17'])

del ob['march 6']
del ob['march 17']
print(ob['march 17'])
