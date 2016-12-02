# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:18:55 2016

@author: Pika
"""
import pandas as pd
import numpy as np
import pyqtgraph as pg

#index col用來設定哪一行要當作col, 是從0開始算的, header指的是該dataframe的columns
data=pd.read_csv('LED_Voltage_Current_Mode1~3.csv',index_col=0, header=14, skip_blank_lines=False)

#加入linear RegionItem的方法
win = pg.GraphicsWindow(title="Basic plotting examples")
p2=win.addPlot(title="Cute")
p2.plot(data.index.values, data.values[:,1],pen='y')
p2.plot(data.index.values, data.values[:,0],pen='g')
p2.showGrid(x=True, y=True)
lr=pg.LinearRegionItem([0,100])
p2.addItem(lr)


def Calculate():
    reg=lr.getRegion()
    print (reg)
    i1=np.where(data.index.values>reg[0])[0][0] # using np.where to get first index
    i2=np.where(data.index.values<reg[1])[0][-1]+1 # using[-1] to get last index, +1 to include the last index    
    print (i1, i2)
    print (data.iloc[i1:i2].index.values)
    print (data.iloc[i1:i2].values) 
    print ("x : " +str(data.iloc[i1:i2].index.values[0])+" ~ "+ str(data.iloc[i1:i2].index.values[-1]))
    print ("y : " +str(data.iloc[i1:i2].values[:,1].min())+" ~ "+ str(data.iloc[i1:i2].values[:,1].max()))
    print ("y mean: "+str(data.iloc[i1:i2].values[:,1].mean()))
    
lr.sigRegionChanged.connect(Calculate)

