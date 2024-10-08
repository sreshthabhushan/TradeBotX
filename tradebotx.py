# -*- coding: utf-8 -*-
"""TradeBotX.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/135lid9LvYSc6VgHE9bWfkBUM3zLIj6Zq

## **Import Libraries**
"""

import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import yfinance as yf

"""## **Google's stock data**"""

# Get Google's stock data from yahoo finance
stock = yf.Ticker("GOOG")
data = stock.history(period="1y")
print(data.head())

"""## **Calculation of Momentum**"""

# Calculation of momentum
data['momentum'] = data['Close'].pct_change()

"""## **Buying/Selling Markers**"""

# Creating subplots to show momentum and buying/selling markers
figure = make_subplots(rows=2, cols=1)
figure.add_trace(go.Scatter(x=data.index,
                         y=data['Open'],
                         name='Open Price'))
figure.add_trace(go.Scatter(x=data.index,
                         y=data['Close'],
                         name='Close Price'))
figure.add_trace(go.Scatter(x=data.index,
                         y=data['momentum'],
                         name='Momentum',
                         yaxis='y2'))
figure.update_layout(title='Algorithmic Trading - Buying/Selling Markers',
                  xaxis_title='Date',
                  yaxis_title='Price')

"""## **Buy & Sell Signals**"""

# Adding the buy and sell signals
figure.add_trace(go.Scatter(x=data.loc[data['momentum'] > 0].index,
                         y=data.loc[data['momentum'] > 0]['Close'],
                         mode='markers', name='Buy',
                         marker=dict(color='green', symbol='triangle-up')))

figure.add_trace(go.Scatter(x=data.loc[data['momentum'] < 0].index,
                         y=data.loc[data['momentum'] < 0]['Close'],
                         mode='markers', name='Sell',
                         marker=dict(color='red', symbol='triangle-down')))

figure.update_layout(title='Algorithmic Trading - Buy & Sell Signals',
                  xaxis_title='Date',
                  yaxis_title='Price')
figure.update_yaxes(title="Momentum", secondary_y=True)
figure.show()