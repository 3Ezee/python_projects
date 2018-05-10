# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:33:39 2018

@author: Ezequiel
"""

import datetime

class ItemRecord:
        
    def __init__(self,tag,amount,obs):
        self._tag = tag
        self._amount = amount
        self._obs = obs
        self._date = datetime.date.today()

    def get_tag(self):
        return self._tag

    def set_tag(self, tag):
        self._tag = tag
        
    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount
    
    def get_obs(self):
        return self._obs

    def set_obs(self, obs):
        self._obs = obs
        
    def get_date(self):
        return self._date
    
    def get_item(self):
        return self._tag +","+ str(self._amount) +","+self._obs +","+ str(self._date)