"""
Demo of the histogram (hist) function with a few features.
In addition to the basic histogram, this demo shows a few optional features:
    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the integral of
      the histogram is 1. The resulting histogram is a probability density.
    * Setting the face color of the bars
    * Setting the opacity (alpha value).
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

elevpath = r"C:\temp\spaLab\elevClim.gdb\USA_elevation_meters"
inMaskData = r"C:\temp\spaLab\elevClim.gdb\sample1"

# Execute ExtractByMask
outExtractByMask = ExtractByMask(elevpath, inMaskData)

arr = arcpy.RasterToNumPyArray(outExtractByMask,nodata_to_value=-9999)

x = arr[np.where(arr != -9999)]

print np.max(x);

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
# add a 'best fit' line - This only applicable to normal
#y = mlab.normpdf(bins, mu, sigma)
#plt.plot(bins, y, 'r--')
plt.xlabel('Elevation')
plt.ylabel('Frequency')
plt.title(r'Histogram of Elevation in NA')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.savefig('c:/temp/test.png')
