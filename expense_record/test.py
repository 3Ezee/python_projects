# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:00:26 2018

@author: Ezequiel
"""

from ItemRecord import ItemRecord

class listItems:
   
    def AddToList(self,tag,amount,obs):
        myobjectx = ItemRecord(tag,amount,obs)
        self._items.add(myobjectx)
    
    
mylist = listItems()

listItems.AddToList("gasto",150,"alquiler","asdas")
        
myobjectx = ItemRecord("gasto",100,"comida")

myobjectx.set_tag("prueba")
print(myobjectx.get_tag())
myobjectx.set_amount(150)
print(myobjectx.get_amount())
print(myobjectx.get_obs())
print(myobjectx.get_date())

myobjecty = ItemRecord("Varios",100,"")
print(myobjecty.get_tag())
print(myobjecty.get_amount())
print(myobjecty.get_obs())

myobjecty.set_amount(150)

print(myobjectx.get_item())




