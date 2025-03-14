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


# example data, you could use any data.
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

# note x is a numpy array but a list works just as well
print(x)

num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
# add a 'best fit' line - This only applicable to normal
#y = mlab.normpdf(bins, mu, sigma)
#plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Frequency')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
