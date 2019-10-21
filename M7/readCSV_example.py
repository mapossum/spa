#https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv

import numpy as np
import urllib.request as rq
import json
import pandas as pd
import arcpy
import numpy as np

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
f = rq.urlopen(url)

#This is how to read a CSV into a numpy array that ArcGIS can read
#First read the file in using Pandas,
#then fill any missing values with a value of your choice
#Finally read pandas data frame into a numpy array and read the headers to the dypes
eqsdata = pd.read_csv(f).fillna(0)
eqsarray = np.array(np.rec.fromrecords(eqsdata.values))
eqsarray.dtype.names = tuple(eqsdata.dtypes.index.tolist())

arcpy.da.NumPyArrayToFeatureClass(eqsarray, r"c:\temp\test5.shp", ("latitude", "longitude"))

