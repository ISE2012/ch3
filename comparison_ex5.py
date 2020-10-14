# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:38 2020

@author: xyz
"""

a = 4
b = 5
c = 6
d = True
e = False

bool1 = d and (a > b)
bool2 = (not d) or (b != c)
bool3 = (d and (not e)) or (a > b)
bool4 = (a%b==2) and ((not d) or e)

print(bool1, bool2, bool3, bool4)






