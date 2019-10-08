#https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv

import numpy as np
import urllib.request as rq
import json


url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
f = rq.urlopen(url)

eqs = json.load(f)

print(eqs["features"][0])


