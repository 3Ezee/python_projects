# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 06:55:05 2018

@author: Ezequiel
"""

import pandas as pd

#lineaHeader = ["WKT","ID","LINEA","TIPO_SERVICIO","RAMAL","SENTIDO"]
#users = pd.read_table('recorrido-colectivos.csv', engine='python', sep=';', header=None, names=lineaHeader)
lineas = pd.read_table('recorrido-colectivos.csv', engine='python', sep=';')
df = pd.DataFrame(lineas)

df['WKT'] = df['WKT'].map(lambda x: x.lstrip('LINESTRING (').rstrip(')'))
coordenadas_series = df['WKT'].str.split(',').apply(pd.Series,1).stack()
coordenadas_series.index = coordenadas_series.index.droplevel(-1)
coordenadasdf = pd.DataFrame(coordenadas_series)
print(coordenadasdf)

newcols = { 0:'WKT'}

coordenadasdf.rename(columns=newcols, inplace=True)
del df['WKT']
df['WKT'] = ''
dfnew = df.join(coordenadasdf)
coordenadasdf_reset = coordenadasdf.reset_index(level=0, drop=True)

df.join(coordenadasdf, lsuffix='_df', rsuffix='_coordenadasdf')

coordenadasdf.join(df)
print(df)

df.to_csv('myDataFrame2.csv')
dfnew.to_csv('myDataFrame2.csv')
df.columns
print(dfnew.index)

dfnew.unstack()