# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:18:55 2016

@author: Pika
"""


import pandas as pd
import numpy as np
import pyqtgraph as pg

#如果不設定index 和header, 預設會把所有東西都弄進來, 會有文字和一大堆nan
csvFile=pd.read_csv('LED_Voltage_Current_Mode1~3.csv',index_col=None, header=None)

#目前發現如果第一行最後沒有逗號, index_col=None, header=None會發生問題, 目前還找不到解決法

#預設不會skip空白的行, 若設定skip_blank_lines=False則可以把空白也算近行數, 這樣就不會發生和excel行數對不上的問題
csvFile=pd.read_csv('LED_Voltage_Current_Mode1~3.csv',index_col=0, header=0, skip_blank_lines=False)

#index col用來設定哪一行要當作col, 是從0開始算的, header指的是該dataframe的columns
data=pd.read_csv('LED_Voltage_Current_Mode1~3.csv',index_col=0, header=20)
#長成這樣 Index(['CH1', 'CH2', 'CH3', 'CH4'], dtype='object')
data.columns

#簡單的取data方法
print(data[:,0].values)

#pyqtgrah 的畫法1, 直接去取需要的該columns, 類似matlab語法, 然後用.values轉成numpy array, 這樣畫會沒有X軸
pg.plot(data.iloc[:,0].values,pen='y' )   # data can be a list of values or a numpy array
#pyqtgrah 的畫法2, x軸取data.index然後轉成numpy array, data的部分先轉成numpy array再一樣用類似matlab的語法取想要的位置
#index長成這樣 Float64Index([ -5.0,  -5.0,  -5.0,  -5.0,  -5.0,  -5.0, -4.99, -4.99, -4.99,
data.index 
pg.plot(data.index.values,data.values[:,1])

#可以直接把numpy array丟進去dataframe裡面, 他會是空index, 空columns的dataframe
newData=pd.DataFrame(data.values)

#Dataframe可以直接用matplotlib 畫plot與hist
data.plot()
data.hist()

#加入linear RegionItem的方法
win = pg.GraphicsWindow(title="Basic plotting examples")
p2=win.addPlot(title="Cute")
p2.plot(data.index.values, data.values[:,2])
p2.addItem(pg.LinearRegionItem([0,100]))

