# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:57:15 2015

@author: SW274998
"""

from math import pi

import pandas as pd

from bokeh.sampledata.stocks import MSFT
from bokeh.plotting import figure, show, output_file

from nsepy.archives import get_price_history
from datetime import date

df = get_price_history(stock = 'SBIN', start = date(2015,8,1),
                            end = date(2015,9,24))
df["Date"] = pd.to_datetime(df.index)

mids = (df.Open + df.Close)/2
spans = abs(df.Close-df.Open)

inc = df.Close > df.Open
dec = df.Open > df.Close
w = 12*60*60*1000 # half day in ms

output_file("candlestick.html", title="candlestick.py example")

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, toolbar_location="left")

p.segment(df.Date, df.High, df.Date, df.Low, color="black")
p.rect(df.Date[inc], mids[inc], w, spans[inc], fill_color="#00FF00", line_color="black")
p.rect(df.Date[dec], mids[dec], w, spans[dec], fill_color="#F2583E", line_color="black")

p.title = "SBIN"
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

show(p)  # open a browser