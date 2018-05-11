# coding: utf-8
"""
Created on Mon May 10 20:56:32 2018

@author: Ezequiel
"""

class Point:
    a = 0 #ax³
    b = 0 #bx²
    c = 0 #cx
    d = 0 #d

    # ax³ + bx² + cx + dn = y
    def GetY(self,x):
        return self.a*x*x*x +self.b*x*x +self.c*x +self.d 

