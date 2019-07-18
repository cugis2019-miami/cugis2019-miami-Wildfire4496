# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:04:18 2019

@author: admin
"""
import pandas
dir(pandas)

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

#plot name on x axis
#plot age of y axis

studentallinfodf=[["Steve",32, "male"],["Lia", 28,"female"],["Vin", 45, "male"],["Katie", 38,"female"]]

df = pandas.DataFrame(studentallinfodf, columns=["name", "age", "gender"],index=[1,2,3,4])
print(df)

agename= go.Bar(x=df["name"], y=df["age"])

plot([agename])

peopleage=[["{Ianshe", 14,"female"], ["Reanna", 14, "female"], ["Ashley",16,"female"]]

import pands as pd
from plotly.offline import plot
import plotly.graph_graphs as go

df=

import go

