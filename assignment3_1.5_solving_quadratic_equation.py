# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:09:59 2020

@author: Administrator
"""


#write apython program to solve quadratic eqation
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
d = (b**2) - (4*a*c)   
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))