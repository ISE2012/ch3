# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:34:20 2020

@author: @justudin
"""

a = 10
b = 20
c = 30

ex1 = a>b or c<b
ex2 = a+b <= c+1 or b>c
ex3 = a==c or b + 10 <= a or c/3==a

print(ex1, ex2, ex3)
# True True True