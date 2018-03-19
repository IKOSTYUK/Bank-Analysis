# Importing Data

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

url = "http://www.fdic.gov/bank/individual/failed/banklist.csv"
url1 = "http://notebook.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv"

bank_data=pd.read_csv(url, parse_dates=[6], index_col = False)
lat_long = pd.read_csv(url1, index_col = False)

# Working With the Data

bank_data["key"] = bank_data["City"].map(str) + bank_data["ST"]
bank_data = bank_data[['Bank Name','key']]

lat_long = lat_long.rename(columns = {'state':'ST'})
lat_long["key"] = lat_long["city"].map(str) + lat_long["ST"]

lat_long = lat_long[['key', 'latitude', 'longitude']]
lat_long1 = lat_long.drop_duplicates(subset=['key'], keep = 'last')

# Merging on Key and Mapping Lat & Lon

data = bank_data.merge(lat_long1, on='key', how='left')
data1 = data[['Bank Name', 'latitude', 'longitude']]
data1 = data1.rename(columns = {'latitude':'lat'})
data1 = data1.rename(columns = {'longitude':'lon'})
data1 = data1.rename(columns = {'Bank Name':'name'})
data2 = data1.dropna()

geoplotlib.dot(data2)
geoplotlib.show()
