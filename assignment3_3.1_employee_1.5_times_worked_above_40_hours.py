# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:24:12 2020

@author: Administrator
"""

#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = float (input("How many hours did you work this month?\n"))
rate = float(input("What is your pay rate?\n"))
if hours<= 40 :
  pay = hours * rate
  print("Pay:", pay)
else:
  pay = 40 * rate + (rate * 1.5) * (hours-40)
  print("Pay:", pay)