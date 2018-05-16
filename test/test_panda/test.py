# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:20:21 2018

@author: Ezequiel
"""

import numpy as np
import pandas as pd

data = np.array([['Nombre','Edad'],
                ['Ezequiel',26],
                ['Lujan',25]])

df = pd.DataFrame(pd.DataFrame(data=data[1:,0:],
                  #index=data[1:,0],
                  columns=data[0,0:]))
print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:]))



print(df)
print(len(df.index))
print(data.shape)
pd.DataFrame()
print(df.at[1,'Nombre'])
print(df)
print(df)
df.ix[2] = ['Floppy',10]
df.set_index('Nombre')
df.reset_index(level=0, drop= True)