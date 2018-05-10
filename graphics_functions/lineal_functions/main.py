# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 04:47:51 2018

@author: Ezequiel
"""
import matplotlib.pyplot as plt
import ManagerPoint as mp

point1 = mp.Point()

# 1x + 2 = y
point1.m = 0.5
point1.b = 0

# x = 0

rx = [] 
ry = []
 

for x in range(-10, 10):
    point1.x = x
    rx.append(x)
    ry.append(point1.GetY())


print("x:",rx)
print("y:",ry)



plt.plot(rx,ry)
plt.scatter(rx,ry,s=20)
#plt.xticks(100)
plt.autoscale(tight = False)
plt.show()