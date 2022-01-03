# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:27:07 2021

@author: APARNA
"""

from abc import ABC,abstractmethod
class Order:
    items = []
    quantities= []
    prices = []
    status = "open"
    
    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
        total +=self.quantities[i]*self.prices[i]
        return total



class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self):
    pass

class SMSAuth(Authorizer):
    authorized = False
    
    def verify_code(self,code):
        print(f"verifying code{code}")
        self.authorized = True

    def is_authorized(self)->bool:
        return self.authorized

class NotARobot(Authorizer):
    authorized = False

    def not_a_robot(self):
        print("Not a Robot")
        self.authorized = True
    
    def is_authorized(self)->bool:
        return self.authorized

class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self,order):
        pass

class PaymentProcessor_sms(PaymentProcessor):

    @abstractmethod
    def auth_sms(self,code):
        pass


class credit_pay(PaymentProcessor):
    def __init__(self,security_code):
        self.security_code = security_code
    
    def pay(self,order):
        print("processing credit payment type")
        print(f"Verifying security code:{self.security_code}")
        order.status = "paid"

class debit_pay(PaymentProcessor):
    def __init__(self,security_code,authorizer : SMSAuth):
        self.security_code = security_code
        self.authorizer = authorizer
    
    def pay(self,order):
        if not self.authorizer.is_authorized():
        print("hall")
        raise Exception("Not Authorized")
        print("processing debit payment type")
        print(f"Verifying security code:{self.security_code}")
        order.status = "paid"

class paypal_pay(PaymentProcessor):
    def __init__(self,email,authorizer : SMSAuth):
        self.email = email
        self.authorizer = authorizer
    
    def pay(self,order):
        if not self.authorizer.is_authorized():
        raise Exception ("Not Authorized")
        print("processing debit payment type")
        print(f"Verifying email:{self.email}")
        order.status = "paid"


order = Order()
order.add_item("Keyboard",1,1000)
order.add_item("Mouse",2,2000)
order.add_item("Mobile",1,16000)


authorizer = NotARobot()


processor = debit_pay("100",authorizer)
authorizer.not_a_robot()
processor.pay(order)


#processor.auth_sms("100")

 