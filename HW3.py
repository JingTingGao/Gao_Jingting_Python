# -*- coding: utf-8 -*-
"""
HW3 

@author: jingtinggao
"""
#Overall Comment: Try to stay with a clear format with your code. Explain what kind of problems you are trying to solve. And then
#                 explain in detail.
#2 import the pandas package
import pandas as pd 
#3 read the located file and transform to table
data=pd.read_table('/Users/jingtinggao/Documents/Gao_Jingting_python/iris.data.txt',header=0,sep=',')
#4 display the first ten rows
data.head(n=10)
#4 display the last ten rows
data.tail(n=10)
#5 simple location statistics (Count, Mean, STD, Min, 25%, 50%, 75%, MAX)
data.describe().transpose()
#6 plot a histogram for each of the numeric columns
data.hist()
#6 plot a bar chart for the nominal column
data.class0.value_counts().plot(kind='bar')
