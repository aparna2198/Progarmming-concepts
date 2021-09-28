# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 01:00:28 2021

@author: APARNA
"""

from datetime import datetime 
class Employee:
    hike = 1.04
    
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay  =  pay 
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@gmail.com"
        
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = self.pay*self.hike
    
    @classmethod
    def set_raise_amt(cls,amt):
        cls.hike = amt
    @classmethod
    def from_string(cls,string):
        first,last,pay = string.split("_")
        return cls(first,last,pay)
    
    @staticmethod
    def weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        
class Developer(Employee):
    hike = 2.04
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        if employees is not None:
            self.employees = employees
        else:
            self.employees = []
    
    def add_employees(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employees(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        print(len(self.employees))
        for emp in self.employees:
            print("-->",emp.fullname())

e1 = Employee("Aparna", "Mane",1000000)
e2 = Employee("Vinayak","Magokar",1500000)

string = "Omkar_Gulve_1000070"
e3 = Employee.from_string(string)

print(e3.fullname())
print(e3.hike)

date = datetime.date(2021,9,13)
print(Employee.weekday(date))
# Employee.set_raise_amt(2.02)

print(Employee.hike)
print(e1.hike)
print(e2.hike)


        