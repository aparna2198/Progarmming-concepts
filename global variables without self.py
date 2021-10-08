# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:51:35 2021

@author: APARNA
"""

global a

class Glob:
    def __init__(self):
        self.a = 10
    
    def printa(self):
        print(self.a)
        
    def printaglobal(self):
        global a
        print(a)
a  = 200       
obj = Glob()
obj.printa()
obj.printaglobal()