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

#Get stats from vector dataset and make array

#Open a cursor for the data that we want to make a histogram of - Done below

#use the cursor to loop trough each record (row) in the dataset and store the number in a list

StatsList = []
fc = r"C:\temp\Cityi10_copy.shp"
field = "SCIRCLE"
cursor = arcpy.SearchCursor(fc)
for row in cursor:
    fieldvalue = row.getValue(field)
    StatsList.append(fieldvalue)
    
del row, cursor

#convert our list into an array
vectorStats = np.array(StatsList)

x = vectorStats

# example data
mu = np.mean(x) # mean of distribution
sigma = np.std(x) # standard deviation of distribution
#x = mu + sigma * np.random.randn(10000)
print x

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='red', alpha=0.5)
# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Frequency')
plt.title(r'Histogram of Shape Statistics: $\mu=' + str(mu) + '$, $\sigma=' + str(sigma) +'$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
