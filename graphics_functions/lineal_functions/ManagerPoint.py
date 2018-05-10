# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 04:04:32 2018

@author: Ezequiel
"""

class Point:
    m = 0 #slope
    x = 0 #variable independent
    b = 0 #intercept
    y = 0 #variable independent

    # mx + b = y
    def GetY(self):
        return self.m * self.x + self.b
        
    # (y - b)/ m = x 
    def GetX(self):
        return (self.y - self.b)/self.m
    
    # (y - b)/ x = y 
    def GetM(self):
        return (self.y - self.b)/self.x
    
    # -mx +y= b
    def GetB(self):
        return -self.m * self.x + self.y


