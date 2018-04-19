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

bathy = arcpy.RasterToNumPyArray(r"C:\temp\GOM.gdb\bathy")
bathy = np.reshape(bathy, bathy.size)

b = np.where(bathy != 0)
bathy = bathy[b]

c = np.where(bathy > -6000)
bathy = bathy[c]

x = bathy

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
plt.title(r'Histogram of Bathy: $\mu=' + str(mu) + '$, $\sigma=' + str(sigma) +'$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
