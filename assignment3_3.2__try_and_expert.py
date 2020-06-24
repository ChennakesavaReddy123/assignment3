# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:36:06 2020

@author: Administrator
"""


#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:hours=input("Enter Hours:")
h = input('Enter Hours:')
r = input('Enter Rate:')

try:
  hours = float(h)
  rate = float (r)
  if hours<= 40:
    pay = hours * rate
  else:
    pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
  print("Pay =", pay)
except:
    print("Error, please enter numeric input"2)