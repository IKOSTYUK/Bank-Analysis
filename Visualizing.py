# Visualizing via Bar Graph

%matplotlib inline

import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn
import time
import datetime as dt
import geoplotlib
from geoplotlib.colors import colorbrewer
from geoplotlib.utils import epoch_to_str, BoundingBox, read_csv

df = pd.read_csv(url, parse_dates=[6], index_col = False)
df["Closing Date"] = pd.to_datetime(df["Closing Date"])
df['year'] = df['Closing Date'].dt.year
df['month'] = df['Closing Date'].dt.month

year = pd.pivot_table(df, index= 'year', values= "City", aggfunc='count')

state = pd.pivot_table(df, index= 'ST', values= "Bank Name", aggfunc='count')
state = state.sort_values(ascending=False)[:17]
state.plot(kind= 'bar', title = 'Bank Failure by State, Year: 2000-2017')

year = pd.pivot_table(df, index= 'year', values= "City", aggfunc='count')
year.plot(kind= 'bar', title = 'Bank Failure by Year')
