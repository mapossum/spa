import numpy as np
import urllib.request as rq
import json

turtleID = 1
url = 'http://geo.conserveturtles.org/Tracking/GetTurtleLocationsByIdAsJson?id={}'.format(turtleID)
f = rq.urlopen(url)

turtledata = json.load(f)
#First Turtle Location
print(turtledata[0])

